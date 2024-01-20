from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.serializers.organization import OrganizationUserSerializer
from events.models.organization import Organization


class OrganizationViewSet(viewsets.ModelViewSet):
    """ViewSet for the Organization model."""
    queryset = Organization.objects.all()
    serializer_class = OrganizationUserSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        title = self.request.data.get('title', '')
        description = self.request.data.get('description', '')
        address = self.request.data.get('address', '')
        postcode = self.request.data.get('postcode', '')

        instance = serializer.save(
            title=title,
            description=description,
            address=address,
            postcode=postcode,
        )
        serializer = OrganizationUserSerializer(instance)
        return Response(serializer.data)
