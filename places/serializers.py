from rest_framework import serializers
from .models import Place, PlaceImage

class PlaceImageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = PlaceImage
        fields = ('position', 'url')

    def get_url(self, obj):
        request = self.context.get('request')
        url = obj.image.url
        return request.build_absolute_uri(url) if request else url

class PlaceSerializer(serializers.ModelSerializer):
    images = PlaceImageSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = (
            'id', 'title', 'slug',
            'short_description', 'long_description',
            'latitude', 'longitude',
            'images',
        )
