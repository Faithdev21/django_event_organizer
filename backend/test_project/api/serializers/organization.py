from typing import Tuple

from rest_framework import serializers

from events.models.organization import Organization


class OrganizationSerializer(serializers.ModelSerializer):
    """Show organizations for the events requests."""
    members = serializers.SerializerMethodField()
    full_address = serializers.SerializerMethodField()

    class Meta:
        model = Organization
        fields: Tuple[str, ...] = (
            "id",
            "title",
            "description",
            "full_address",
            "members",
        )

    def get_members(self, obj):
        from api.serializers.user import CustomUserEventSerializer
        members_queryset = obj.members.all()
        serializer = CustomUserEventSerializer(members_queryset, many=True, read_only=True)

        return serializer.data

    def get_full_address(self, obj):
        return f"{obj.address}, {obj.postcode}"


class OrganizationUserSerializer(OrganizationSerializer):
    """Create organization."""
    class Meta:
        model = Organization
        fields: Tuple[str, ...] = (
            "id",
            "title",
            "description",
            "full_address",
        )
