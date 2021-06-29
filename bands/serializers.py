from rest_framework import serializers
from .models import Band


class BandSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ("id", "reviewer", "name", "description", "created_at")
    model = Band