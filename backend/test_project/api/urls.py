from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views.event import EventViewSet
from api.views.organization import OrganizationViewSet
from api.views.user import UserListView

app_name = "api"

router_v1 = DefaultRouter()
router_v1.register("organizations", OrganizationViewSet)
router_v1.register("events", EventViewSet)
router_v1.register("users", UserListView)

urlpatterns = [
    path("v1/auth/", include("djoser.urls")),
    path("v1/auth/", include("djoser.urls.jwt")),
    path("v1/", include(router_v1.urls)),
]
