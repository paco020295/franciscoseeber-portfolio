import json
from collections import Counter
from pathlib import Path

from django.db.models.functions import Length
from django.http import JsonResponse
from django.views.generic import View
from .models import Review
from django.http import JsonResponse
from django.core import serializers


class JsonReviewsView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        reviews = Review.objects.all().filter(client_country=request.GET.get("country")).order_by(Length('review_text').desc())
        data = serializers.serialize('json', reviews, fields=('id', 'client_name', 'average_score'))
        return JsonResponse({'data': data}, safe=False)


class JsonReviewView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        review_id = request.GET.get("review_id")
        reviews = Review.objects.get(id=review_id)
        data = serializers.serialize('json', [reviews, ], fields=(
            'title',
            'average_score',
            'skills',
            'quality',
            'availability',
            'deadlines',
            'communication',
            'cooperation',
            'review_text'
        ))
        return JsonResponse({'data': data}, safe=False)


class JsonMapView (View):
    @staticmethod
    def get(*args, **kwargs):
        geojson = f"{Path(__file__).parent}/data/ne_110m_admin_0_countries.geojson"
        with open(geojson, 'r', encoding='utf-8') as fjson:
            raw_data = json.load(fjson)

        countries_dict = Review.objects.values_list('client_country', flat=True)
        countries_count = dict(Counter(list(countries_dict)))
        for idx, features in enumerate(raw_data['features']):
            iso_a2 = features['properties']['iso_a2']
            if iso_a2 in countries_count:
                raw_data['features'][idx]['properties']['count'] = countries_count[iso_a2]
        return JsonResponse(raw_data, safe=False)
