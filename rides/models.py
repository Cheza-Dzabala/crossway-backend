from django.db import models
from vehicles.models import Vehicle
from django.contrib.gis.db import models as gis_models 


# Create your models here.

class Ride(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='rides')
    departure = models.DateTimeField()
    estimated_duration = models.DurationField()
    estimated_arrival = models.DateTimeField()
    departure_location = gis_models.PointField()
    arrival_location = gis_models.PointField()
    is_active = models.BooleanField(default=False)
    capacity = models.IntegerField()
    

    
    def __str__(self):
        return f"{self.vehicle.license_plate} - {self.departure}"
    
    
    