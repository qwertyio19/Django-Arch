from django.utils.timezone import now
from apps.base.models import Visitor, PageVisit


class TrackVisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip_address = request.META.get('REMOTE_ADDR')
        page_name = request.path

        visitor, created = Visitor.objects.get_or_create(ip_address=ip_address)
        if not created:
            visitor.last_visit = now()
        else:
            visitor.visit_count = 1
        visitor.save()

        PageVisit.objects.create(page=page_name)

        response = self.get_response(request)
        return response
