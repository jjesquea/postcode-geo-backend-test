from rest_framework import viewsets

from postcodeGeoApp.postcode.models import Coordinate
from postcodeGeoApp.postcode.serializers.coordinates import CoordinateSerializer


class CoordinateViewSet(viewsets.ModelViewSet):
    """Coordinate ViewSet"""

    serializer_class = CoordinateSerializer
    queryset = Coordinate.objects.all()
