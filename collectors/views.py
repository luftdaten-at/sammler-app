from django.urls import path
from django.views.generic import ListView
from .models import Location


class LocationList(ListView):
    queryset = Location.objects.filter(point__isnull=False)