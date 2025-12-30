# apps/base/middleware.py
import logging
from datetime import timedelta
from urllib.parse import urlparse

from django.conf import settings
from django.db.models import F
from django.utils import timezone

from apps.base.models import Visitor, PageVisit

logger = logging.getLogger("stats")


class TrackVisitorMiddleware:
    SESSION_TTL = timedelta(minutes=30)

    SKIP_PREFIXES = ("/admin/", "/static/", "/media/")
    SKIP_EXACT = ("/api/v1/stats/",)

    def __init__(self, get_response):
        self.get_response = get_response

    def _get_client_ip(self, request) -> str:
        xff = request.META.get("HTTP_X_FORWARDED_FOR")
        if xff:
            return xff.split(",")[0].strip()

        x_real = request.META.get("HTTP_X_REAL_IP")
        if x_real:
            return x_real.strip()

        return (request.META.get("REMOTE_ADDR") or "").strip()

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
        verbose = getattr(settings, "STATS_LOG_VERBOSE", False)

        if request.method not in ("GET", "HEAD"):
            if verbose:
                logger.debug("SKIP method=%s path=%s", request.method, request.path)
            return self.get_response(request)

        path = request.path
        if self._should_skip(path):
            if verbose:
                logger.debug("SKIP path=%s", path)
            return self.get_response(request)

        now = timezone.now()

        ip = self._get_client_ip(request)
        if not ip:
            logger.warning("NO_IP path=%s meta_remote=%s", path, request.META.get("REMOTE_ADDR"))
            return self.get_response(request)

        page_name = self._get_page_name(request)

        if verbose:
            logger.debug(
                "REQ path=%s page=%s ip=%s remote=%s xff=%s xreal=%s ua=%s",
                path,
                page_name,
                ip,
                request.META.get("REMOTE_ADDR"),
                request.META.get("HTTP_X_FORWARDED_FOR"),
                request.META.get("HTTP_X_REAL_IP"),
                request.META.get("HTTP_USER_AGENT"),
            )

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

            logger.info(
                "COUNTED new_session=1 created=%s ip=%s page=%s path=%s visitor_id=%s",
                created,
                ip,
                page_name,
                path,
                visitor.pk,
            )
        else:
            Visitor.objects.filter(pk=visitor.pk).update(last_visit=now)

            if verbose:
                logger.debug(
                    "NOT_COUNTED new_session=0 ip=%s page=%s path=%s visitor_id=%s last_visit=%s",
                    ip,
                    page_name,
                    path,
                    visitor.pk,
                    visitor.last_visit,
                )

        return self.get_response(request)
