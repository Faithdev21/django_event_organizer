from rest_framework import generics

from api.serializers import CustomUserSerializer
from users.models import User


class UserListView(generics.ListCreateAPIView):
    """API view for listing and creating users."""

    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
