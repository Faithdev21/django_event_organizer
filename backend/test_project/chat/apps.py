from django.apps import AppConfig


class ChatConfig(AppConfig):
    """AppConfig for the chat app."""

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "chat"
