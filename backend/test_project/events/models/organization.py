from django.db import models


class Organization(models.Model):
    """Model representing organization."""
    title = models.CharField(max_length=255)
    description = models.TextField()
    address = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"
        ordering = ("title",)

    def __str__(self):
        return self.title
