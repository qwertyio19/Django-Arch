from rest_framework.routers import DefaultRouter
from apps.notifications.views import TypeNotificationView, NotificationView


router = DefaultRouter()
router.register(r"type", TypeNotificationView, basename="type")
router.register(r"notification", NotificationView, basename="notification")


urlpatterns = router.urls