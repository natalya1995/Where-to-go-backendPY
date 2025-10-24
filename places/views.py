from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Place
from .serializers import PlaceSerializer

class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Place.objects.filter(is_published=True).prefetch_related('images')
    serializer_class = PlaceSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'short_description', 'long_description']
    filterset_fields = ['is_published']
