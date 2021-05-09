from rest_framework import serializers

from postcodeGeoApp.postcode.models import Coordinate


class CoordinateSerializer(serializers.ModelSerializer):
    """Coordinate model serializer """

    class Meta:
        model = Coordinate
        fields = '__all__'
        read_only_fields = ('uuid', 'created_at', 'updated_at')
