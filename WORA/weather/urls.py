from django.urls import path
from .views import WeatherAPIView, WeatherHistoryAPIView

urlpatterns = [
    path('', WeatherAPIView.as_view(), name='weather-api'),
    path('history/', WeatherHistoryAPIView.as_view(), name='weather-history'),
]
