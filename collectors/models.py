from django.db import models
from django.contrib.gis.db.models import PointField


class Location(models.Model):
    name = models.CharField(max_length=255)
    point = PointField()
    
    @property
    def lat_lng(self):
        return list(getattr(self.point, 'coords', []) [::-1])
    

class Collector(models.Model):
    name = models.CharField(max_length=12)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)