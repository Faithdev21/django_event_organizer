from django.contrib import admin

from events.models.event import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Admin configuration for the Event model."""
    list_display = ('title', 'description', 'date', 'image_preview',)
    search_fields = ('title', 'description', 'organizations__title',)

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True
