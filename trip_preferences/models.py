from django.db import models
from drivers.models import Driver
from rides.models import Ride
# Create your models here.

class TripPreferences(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
class RidePreference(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='preferences')
    preference = models.ForeignKey(TripPreferences, on_delete=models.CASCADE, related_name='driver_preferences')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.user.name} - {self.preference.name}"
    

