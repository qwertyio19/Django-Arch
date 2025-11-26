from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.yasg import urlpatterns_yasg

# Основные маршруты (не зависят от мультиязычности)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urlpatterns_yasg)),
]


# Маршруты, зависящие от языка (i18n)
urlpatterns += i18n_patterns(
    path('api/v1/kenesh/', include('apps.kenesh.urls')),
    path('api/v1/notifications/', include('apps.notifications.urls')),
    path('api/v1/news/', include('apps.news.urls')),
    path('api/v1/base/', include('apps.base.urls')),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
