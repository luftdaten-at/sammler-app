from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Location


@admin.register(Location)
class LocationAdmin(OSMGeoAdmin):
    default_lon = 1824950
    default_lat = 6143058
    default_zoom = 12

