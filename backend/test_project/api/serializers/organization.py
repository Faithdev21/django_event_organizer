from typing import Tuple

from rest_framework import serializers

from events.models.organization import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    """Serializer for the Organization model."""

    class Meta:
        model = Organization
        fields: Tuple[str, ...] = (
            "id",
            "title",
            "description",
            "address",
            "postcode",
        )
