import logging
from datetime import timedelta

from django.conf import settings
from django.db.models import F
from django.utils import timezone

from apps.base.models import Visitor, PageVisit

logger = logging.getLogger("stats")


class TrackVisitorMiddleware:
    SESSION_TTL = timedelta(minutes=15)

    SKIP_EXACT = ("/api/v1/stats/",)
    SKIP_PREFIXES = ("/admin/", "/static/", "/media/")

    def __init__(self, get_response):
        self.get_response = get_response

    def _should_skip(self, path: str) -> bool:
        if path in self.SKIP_EXACT:
            return True
        return any(path.startswith(p) for p in self.SKIP_PREFIXES)

    def _get_client_ip(self, request) -> str:
        xff = request.META.get("HTTP_X_FORWARDED_FOR")
        if xff:
            return xff.split(",")[0].strip()

        x_real = request.META.get("HTTP_X_REAL_IP")
        if x_real:
            return x_real.strip()

        return (request.META.get("REMOTE_ADDR") or "").strip()

    def __call__(self, request):
        verbose = getattr(settings, "STATS_LOG_VERBOSE", False)

        if request.method not in ("GET", "HEAD"):
            return self.get_response(request)

        path = request.path
        if self._should_skip(path):
            return self.get_response(request)

        now = timezone.now()
        ip = self._get_client_ip(request)

        if not ip:
            logger.warning("NO_IP path=%s remote=%s", path, request.META.get("REMOTE_ADDR"))
            return self.get_response(request)

        visitor, created = Visitor.objects.get_or_create(
            ip_address=ip,
            defaults={"visit_count": 1, "last_visit": now},
        )

        if created:
            PageVisit.objects.create(page="/", timestamp=now)
            logger.info("COUNTED created=1 ip=%s path=%s", ip, path)
            return self.get_response(request)

        threshold = now - self.SESSION_TTL

        updated = Visitor.objects.filter(
            pk=visitor.pk,
            last_visit__lt=threshold,
        ).update(
            visit_count=F("visit_count") + 1,
            last_visit=now,
        )

        if updated == 1:
            PageVisit.objects.create(page="/", timestamp=now)
            logger.info("COUNTED created=0 ip=%s path=%s", ip, path)
        else:
            Visitor.objects.filter(pk=visitor.pk).update(last_visit=now)
            if verbose:
                logger.debug("NOT_COUNTED ip=%s path=%s", ip, path)

        return self.get_response(request)
