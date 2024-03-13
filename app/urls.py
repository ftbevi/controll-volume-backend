from django.contrib import admin
from django.urls import path

admin.site.site_header = "Controll Store"

urlpatterns = [
    path('admin/', admin.site.urls),
]
