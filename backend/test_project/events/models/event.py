from django.db import models
from django.utils.safestring import mark_safe

from events.models.organization import Organization


class Event(models.Model):
    """Model representing event."""
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    organizations = models.ManyToManyField(Organization, related_name='events')
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    date = models.DateTimeField()

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ("-date",)

    @property
    def image_preview(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.image.url}" width="300" height="300" />')

    def __str__(self):
        return self.title
