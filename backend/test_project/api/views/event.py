import asyncio

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from api.serializers import EventSerializer
from events.models.event import Event


class EventViewSet(viewsets.ModelViewSet):
    """ViewSet for the Event model."""
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ("date",)
    search_fields = ("title", "organizations__title",)
    ordering_fields = ("date",)

    async def perform_create(self, serializer) -> None:
        """60 seconds sleep after creating."""
        await asyncio.sleep(60)
        serializer.save()
