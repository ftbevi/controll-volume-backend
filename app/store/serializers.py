from rest_framework import serializers

from .models import TrashStations


class TrashStationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrashStations
        fields = ['__all__']
