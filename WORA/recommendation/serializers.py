from rest_framework import serializers
from .models import Recommendation

class RecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendation
        fields = ['id', 'search', 'outfit_text', 'created_at']
        read_only_fields = ['search', 'outfit_text', 'created_at']
