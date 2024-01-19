from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Admin configuration for the User model."""
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
