from datetime import timedelta
from urllib.parse import urlparse

from django.db.models import F
from django.utils import timezone

from apps.base.models import Visitor, PageVisit


class TrackVisitorMiddleware:
    """
    Логика:
    - Находим реальный IP (X-Forwarded-For / X-Real-IP / REMOTE_ADDR)
    - НЕ считаем тех. эндпоинты (stats, admin, static, media...)
    - Считаем total_views не на каждый запрос, а 1 раз за SESSION_TTL
      (то есть за одну "сессию" посетителя).
    """

    SESSION_TTL = timedelta(minutes=30)

    SKIP_PREFIXES = (
        "/admin/",
        "/static/",
        "/media/",
    )
    SKIP_EXACT = (
        "/api/v1/stats/",
    )

    def __init__(self, get_response):
        self.get_response = get_response

    def _get_client_ip(self, request) -> str:
        xff = request.META.get("HTTP_X_FORWARDED_FOR")
        if xff:
            return xff.split(",")[0].strip()

        x_real = request.META.get("HTTP_X_REAL_IP")
        if x_real:
            return x_real.strip()

        return request.META.get("REMOTE_ADDR", "").strip()

    def _get_page_name(self, request) -> str:
        referer = request.META.get("HTTP_REFERER")
        if referer:
            try:
                return urlparse(referer).path or request.path
            except Exception:
                return request.path
        return request.path

    def _should_skip(self, path: str) -> bool:
        if path in self.SKIP_EXACT:
            return True
        return any(path.startswith(p) for p in self.SKIP_PREFIXES)

    def __call__(self, request):
        if request.method not in ("GET", "HEAD"):
            return self.get_response(request)

        path = request.path
        if self._should_skip(path):
            return self.get_response(request)

        now = timezone.now()
        ip = self._get_client_ip(request)
        if not ip:
            return self.get_response(request)

        page_name = self._get_page_name(request)

        visitor, created = Visitor.objects.get_or_create(
            ip_address=ip,
            defaults={"visit_count": 0, "last_visit": now},
        )

        is_new_session = created or (now - visitor.last_visit) > self.SESSION_TTL

        if is_new_session:
            Visitor.objects.filter(pk=visitor.pk).update(
                visit_count=F("visit_count") + 1,
                last_visit=now,
            )
            PageVisit.objects.create(page=page_name, timestamp=now)
        else:
            Visitor.objects.filter(pk=visitor.pk).update(last_visit=now)

        return self.get_response(request)
