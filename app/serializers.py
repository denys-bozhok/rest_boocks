from rest_framework import serializers
from .models import Boock


class SerializedHome(serializers.ModelSerializer):
    class Meta:
        model = Boock
        fields = ('tittle', 'rating', 'description', 'date', 'slug')