from django.db import models
from weather.models import WeatherSearch

# Create your models here.

class Recommendation(models.Model):
    search = models.OneToOneField(
        WeatherSearch,
        on_delete=models.CASCADE,
        related_name='recommendation'
    )
    outfit_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.outfit_text[:30]
