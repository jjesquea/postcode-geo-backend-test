from rest_framework import routers

from postcodeGeoApp.postcode.views.coordinates import CoordinateViewSet

router = routers.DefaultRouter()
router.register('coordinates', CoordinateViewSet, basename='coordinates')

coordinate_urls = router.urls
