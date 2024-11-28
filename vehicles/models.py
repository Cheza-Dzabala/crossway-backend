from django.db import models
from drivers.models import Driver 
# Create your models here.
class Vehicle(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='vehicles')
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100, unique=True)
    blue_book = models.ImageField(upload_to='blue_books/')
    capacity = models.IntegerField()
    mileage_at_registration = models.IntegerField()
    mileage_at_last_service = models.IntegerField()
    
    
    class Conditions(models.TextChoices):
        GOOD = 'good', 'Good'
        POOR = 'poor', 'Poor'
        AVERAGE = 'average', 'Average'
        BAD = 'bad', 'Bad'
    
    condition = models.CharField(
        max_length=10,
        choices=Conditions.choices,
        default=Conditions.GOOD,
    )

    
    
    def __str__(self):
        return self.license_plate
    

# Vehicle Image model
class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='vehicle_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.vehicle.license_plate}"