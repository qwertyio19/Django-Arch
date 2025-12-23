from apps.base.models import Visit

class VisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        Visit.objects.create(
            ip_address=request.META.get("REMOTE_ADDR"),
            path=request.path
        )
        response = self.get_response(request)
        return response
