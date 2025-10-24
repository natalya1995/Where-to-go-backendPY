from django.http import JsonResponse, Http404
from django.urls import reverse
from .models import Place

def places_geojson(request):
    features = []
    for p in Place.objects.filter(is_published=True).prefetch_related('images'):
        details_url = request.build_absolute_uri(
            reverse('place-details', kwargs={'pk': p.pk})
        )
        features.append({
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [p.longitude, p.latitude]},
            "properties": {"title": p.title, "placeId": str(p.pk), "detailsUrl": details_url},
        })
    return JsonResponse({"type": "FeatureCollection", "features": features})

def place_details(request, pk: int):
    try:
        p = Place.objects.prefetch_related('images').get(pk=pk, is_published=True)
    except Place.DoesNotExist:
        raise Http404("Place not found")

    imgs = [request.build_absolute_uri(i.image.url) for i in p.images.all().order_by('position', 'id')]
    payload = {
        "title": p.title,
        "imgs": imgs,
        "description_short": p.short_description or "",
        "description_long": f"<p>{(p.long_description or '').strip()}</p>",
        "coordinates": {"lat": p.latitude, "lng": p.longitude},
    }
    return JsonResponse(payload)
