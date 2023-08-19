from rest_framework import serializers
from .models import Review


class SerializedReview(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('user', 'text', 'date')