from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.event import EventViewSet
from api.views.organization import OrganizationViewSet

app_name = "api"

router_v1 = DefaultRouter()
router_v1.register("organizations", OrganizationViewSet)
router_v1.register("events", EventViewSet)

urlpatterns = [
    path("v1/auth/", include("djoser.urls")),
    path("v1/auth/", include("djoser.urls.jwt")),
    path("v1/", include(router_v1.urls)),
]
