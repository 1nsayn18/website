from django.db import models
from rest_framework import fields, serializers
from .models import Moviedata

class MovieSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Moviedata
        fields = ['id', 'name', 'duration', 'rating', 'typ', 'image']
