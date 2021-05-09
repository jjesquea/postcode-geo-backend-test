from django.db import models

from postcodeGeoApp.utils.models import PostcodeGeoBase


def coordinate_file_directory_path(instance, filename):
    """ Return the route of coordinate file that will be stored """
    return 'coordinate_{0}/{1}'.format(instance.id, filename)


class Coordinate(PostcodeGeoBase):
    """Coordinate model."""

    upload = models.FileField(
        upload_to=coordinate_file_directory_path,
        max_length=150,
    )
