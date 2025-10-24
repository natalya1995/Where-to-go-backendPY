from django.urls import path
from rest_framework.routers import DefaultRouter

from places.views import PlaceViewSet
from places.geo import places_geojson, place_details

router = DefaultRouter()
router.register(r'places', PlaceViewSet, basename='place')

urlpatterns = [
    path('places-geojson/', places_geojson, name='places-geojson'),
    path('places/<int:pk>/details/', place_details, name='place-details'),
]
urlpatterns += router.urls
