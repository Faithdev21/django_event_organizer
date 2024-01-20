from typing import Tuple

from djoser.serializers import UserCreateSerializer

from api.serializers.organization import OrganizationUserSerializer
from users.models import User


class CustomUserEventSerializer(UserCreateSerializer):
    """Serializer for the events requests."""

    class Meta:
        model = User
        fields: Tuple[str, ...] = (
            "id",
            "email",
            "phone_number",
            "password",
        )
        extra_kwargs: dict = {"password": {"write_only": True}}

    def create(self, validated_data) -> User:
        user = User.objects.create_user(
            email=validated_data["email"],
            phone_number=validated_data.get("phone_number", None),
            password=validated_data["password"],
        )
        return user


class CustomUserSerializer(CustomUserEventSerializer):
    """Serializer for the custom User model."""
    organizations = OrganizationUserSerializer(many=True, required=False)

    class Meta:
        model = User
        fields: Tuple[str, ...] = (
            "id",
            "email",
            "phone_number",
            "organizations",
            "password",
        )
        extra_kwargs: dict = {"password": {"write_only": True}}
