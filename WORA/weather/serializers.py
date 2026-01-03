from rest_framework import serializers
from .models import WeatherSearch

class WeatherSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherSearch
        fields = ['id', 'user', 'city', 'temperature', 'weather_description', 'created_at']
        read_only_fields = ['user', 'temperature', 'weather_description', 'created_at']
