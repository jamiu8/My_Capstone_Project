from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import requests
from django.conf import settings
from .models import WeatherSearch
from .serializers import WeatherSearchSerializer
from rest_framework.request import Request
# Create your views here.

class WeatherAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        city = request.query_params.get('city')
        if not city:
            return Response({"error": "City parameter is required"}, status=400)

        # Call OpenWeatherMap API
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises error if HTTP 4xx/5xx
            data = response.json()
        except requests.exceptions.RequestException as e:
            return Response({"error": "Could not fetch weather data", "details": str(e)}, status=500)

        temperature = data['main']['temp']
        description = data['weather'][0]['description']

        # Save search
        weather_search = WeatherSearch.objects.create(
            user=request.user,
            city=city,
            temperature=temperature,
            weather_description=description
        )

        serializer = WeatherSearchSerializer(weather_search)
        return Response(serializer.data)
    
class WeatherHistoryAPIView(ListAPIView):
    serializer_class = WeatherSearchSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = WeatherSearch.objects.filter(user=self.request.user).order_by('-created_at')

        city = self.request.query_params.get('city')    # type: ignore
        if city:
            queryset = queryset.filter(city__iexact=city)

        return queryset
