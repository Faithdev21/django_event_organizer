from django.apps import AppConfig


class ApiConfig(AppConfig):
    """AppConfig for the API app."""

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "api"
