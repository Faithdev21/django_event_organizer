from typing import Dict, Tuple

from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from api.serializers.image import Base64ImageField
from api.serializers.organization import OrganizationSerializer
from events.models.event import Event


class EventSerializer(serializers.ModelSerializer):
    """Serializer for the Event model."""

    image = Base64ImageField(required=False)

    class Meta:
        model = Event
        fields: Tuple[str, ...] = (
            "id",
            "title",
            "description",
            "organizations",
            "image",
            "date",
        )

    def validate(self, data: Dict) -> Dict:
        organizations = data.get("organizations")

        if not organizations:
            raise serializers.ValidationError("Organization field is required")
        return data

    def create(self, validated_data: Dict) -> ReturnDict:
        instance = super().create(validated_data)
        return instance

    def to_representation(self, instance: Event) -> Dict:
        representation = super().to_representation(instance)
        representation["organizations"] = OrganizationSerializer(
            instance.organizations.all(), many=True
        ).data
        return representation
