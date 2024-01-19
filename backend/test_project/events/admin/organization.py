from django.contrib import admin

from events.models.organization import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    """Admin configuration for the Organization model."""
    list_display = ('title', 'description', 'address', 'postcode',)
