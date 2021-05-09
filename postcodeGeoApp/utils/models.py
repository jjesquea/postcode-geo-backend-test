from uuid import uuid4

from django.db import models


class PostcodeGeoBase(models.Model):
    """Postcode Geolocation base model."""

    uuid = models.UUIDField(default=uuid4, primary_key=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta class."""

        abstract = True
        ordering = ('-created_at', '-updated_at')
