from rest_framework import serializers

from .models import Discarts, Notifications, TrashStations


class DiscartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discarts
        fields = ("user", "quantity", "created_at")


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notifications
        fields = ("checker", "status", "created_at")


class TrashStationsSerializer(serializers.ModelSerializer):
    discarts = DiscartsSerializer(many=True)
    notifications = NotificationsSerializer(many=True)

    class Meta:
        model = TrashStations
        fields = ("title", "quantity_max", "discarts", "volume_percent", "notifications")
