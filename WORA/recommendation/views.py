from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from weather.models import WeatherSearch
from .models import Recommendation
from .serializers import RecommendationSerializer
from .utils import generate_outfit

# Create your views here.

class RecommendationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        city = request.query_params.get('city')
        if not city:
            return Response({"error": "City parameter is required"}, status=400)

        # Find the latest weather search for this city by the user
        try:
            weather_search = WeatherSearch.objects.filter(user=request.user, city__iexact=city).latest('created_at')
        except WeatherSearch.DoesNotExist:
            return Response({"error": "No weather data found for this city."}, status=404)

        # Check if recommendation already exists
        recommendation, created = Recommendation.objects.get_or_create(
            search=weather_search,
            defaults={'outfit_text': generate_outfit(weather_search.temperature, weather_search.weather_description)}
        )

        serializer = RecommendationSerializer(recommendation)
        return Response(serializer.data)
    
class RecommendationHistoryAPIView(ListAPIView):
    serializer_class = RecommendationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Recommendation.objects.filter(
            search__user=self.request.user
        ).order_by('-created_at')
