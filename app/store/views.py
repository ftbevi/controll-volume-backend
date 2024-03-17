from rest_framework import generics

from .models import TrashStations, Notifications
from .serializers import TrashStationsSerializer, NotificationsSerializer


class TrashStationsList(generics.ListAPIView):
    queryset = TrashStations.objects.all()
    serializer_class = TrashStationsSerializer


class NotificationsList(generics.UpdateAPIView):
    queryset = Notifications.objects.all()
    serializer_class = NotificationsSerializer
