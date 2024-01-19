from typing import Tuple

from djoser.serializers import UserCreateSerializer

from users.models import User


class CustomUserSerializer(UserCreateSerializer):
    """Serializer for the custom User model."""

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

    def create(self, validated_data) -> User:
        user = User.objects.create_user(
            email=validated_data["email"],
            phone_number=validated_data.get("phone_number", None),
            password=validated_data["password"],
        )
        return user
