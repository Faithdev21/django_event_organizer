from rest_framework import serializers

from api.serializers.image import Base64ImageField
from api.serializers.organization import OrganizationSerializer
from events.models.event import Event
from events.models.organization import Organization


class EventOrganizationSerializer(serializers.ModelSerializer):
    """Serializer for the Event model with OrganizationSerializer."""
    organizations = OrganizationSerializer(many=True)
    image = Base64ImageField(required=False)

    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "description",
            "organizations",
            "image",
            "date",
        )


class EventSerializer(serializers.ModelSerializer):
    """Serializer for the Event model."""
    organizations = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all(),
        many=True,
        required=True
    )
    image = Base64ImageField(required=False)

    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "description",
            "organizations",
            "image",
            "date",
        )

    def create(self, validated_data):
        organizations_data = validated_data.pop('organizations', [])
        instance = Event.objects.create(**validated_data)
        instance.organizations.set(organizations_data)
        return instance

    def to_representation(self, instance):
        representation = EventOrganizationSerializer(instance).data
        return representation
