from rest_framework import serializers
from .models import data

class dataserializers(serializers.ModelSerializer):
    class Meta:
        model = data
        field = ['id', 'name', 'roll', 'city']