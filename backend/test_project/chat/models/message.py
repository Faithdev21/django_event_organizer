from datetime import datetime

from django.db import models

from chat.models.room import Room
from users.models import User


class Message(models.Model):
    """Model representing a chat message."""

    user = models.ForeignKey(
        User,
        related_name="messages",
        on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        Room,
        related_name="messages",
        on_delete=models.CASCADE
    )
    content: str = models.TextField()
    timestamp: datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("timestamp",)

    def __str__(self) -> str:
        return f"{self.user.email}: {self.content}"
