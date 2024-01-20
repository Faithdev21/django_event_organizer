from rest_framework import viewsets

from api.serializers.user import CustomUserSerializer
from users.models import User


class UserListView(viewsets.ModelViewSet):
    """ViewSet for listing and creating users."""
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
