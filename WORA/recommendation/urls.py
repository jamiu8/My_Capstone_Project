from django.urls import path
from .views import RecommendationAPIView, RecommendationHistoryAPIView

urlpatterns = [
    path('', RecommendationAPIView.as_view(), name='recommendation-api'),
     path('history/', RecommendationHistoryAPIView.as_view(), name='recommendation-history'),
]
