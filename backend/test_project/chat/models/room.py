from django.db import models


class Room(models.Model):
    """Model representing a chat room."""

    name: str = models.CharField(max_length=255, unique=True)
    slug: str = models.SlugField(unique=True)

    def __str__(self) -> str:
        return self.name
