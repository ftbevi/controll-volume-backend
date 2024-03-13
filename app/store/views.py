from rest_framework import generics

from .models import TrashStations
from .serializers import TrashStationsSerializer


class TrashStationsList(generics.ListAPIView):
    queryset = TrashStations.objects.all()
    serializer_class = TrashStationsSerializer
