from django.db import models
from users.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    drivers_license_front = models.ImageField(upload_to='licenses/', null=True, blank=True)
    drivers_license_back = models.ImageField(upload_to='licenses/', null=True, blank=True)
    driver_selfie = models.ImageField(upload_to='selfies/', null=True, blank=True)
    is_profile_complete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    ban_reason = models.CharField(max_length=500, null=False, blank=True, default='')
    
    def __str__(self):
        return self.user.name

