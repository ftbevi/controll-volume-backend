from django.urls import path

from .views import TrashStationsList, NotificationsList

urlpatterns = [
    path(r"", TrashStationsList.as_view()),
    path(r"collect", NotificationsList.as_view()),
]
