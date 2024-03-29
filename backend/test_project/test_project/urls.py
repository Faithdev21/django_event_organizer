from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Event organizer API",
        default_version='v1',
        description="Документация для приложения django_event_organizer",
        contact=openapi.Contact(email="admin@django_event_organizer.ru"),
    ),
    permission_classes=[AllowAny],
    public=True,
)

main_urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path("chat/", include('chat.urls')),
]
docs_urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
]

if settings.DEBUG:
    main_urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
urlpatterns = docs_urlpatterns + main_urlpatterns
