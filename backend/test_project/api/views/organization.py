from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from api.serializers import OrganizationSerializer
from events.models.organization import Organization


class OrganizationViewSet(viewsets.ModelViewSet):
    """ViewSet for the Organization model."""

    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = (IsAuthenticated,)
