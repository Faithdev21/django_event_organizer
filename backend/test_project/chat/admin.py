from django.contrib import admin

from chat.models.message import Message
from chat.models.room import Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    """Admin configuration for the Message model."""


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """Admin configuration for the Room model."""
