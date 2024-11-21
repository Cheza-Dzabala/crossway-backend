from django.db import models
from users.models import User
from django.core.exceptions import ValidationError

# Create your models here.
class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    drivers_license_front = models.ImageField(upload_to='licenses/', null=True, blank=True)
    drivers_license_back = models.ImageField(upload_to='licenses/', null=True, blank=True)
    driver_selfie = models.ImageField(upload_to='selfies/', null=True, blank=True)
    driver_photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    is_profile_complete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    ban_reason = models.CharField(max_length=500, null=True, blank=True)

    
    def clean(self):
        # Validate image fields
        if not self.drivers_license_front:
            raise ValidationError({'drivers_license_front': 'Driver\'s license front image is required.'})
        if not self.drivers_license_back:
            raise ValidationError({'drivers_license_back': 'Driver\'s license back image is required.'})
        if not self.driver_selfie:
            raise ValidationError({'driver_selfie': 'A selfie image is required.'})
        if not self.driver_photo:
            raise ValidationError({'driver_photo': 'A driver photo is required.'})
        
        # Check if these are image files
        if not self.drivers_license_front.name.endswith('.jpg') and not self.drivers_license_front.name.endswith('.png'):
            raise ValidationError({'drivers_license_front': 'Driver\'s license front image must be a JPG or PNG.'})
        if not self.drivers_license_back.name.endswith('.jpg') and not self.drivers_license_back.name.endswith('.png'):
            raise ValidationError({'drivers_license_back': 'Driver\'s license back image must be a JPG or PNG.'})
        if not self.driver_selfie.name.endswith('.jpg') and not self.driver_selfie.name.endswith('.png'):
            raise ValidationError({'driver_selfie': 'A selfie image must be a JPG or PNG.'})
        if not self.driver_photo.name.endswith('.jpg') and not self.driver_photo.name.endswith('.png'):
            raise ValidationError({'driver_photo': 'A driver photo must be a JPG or PNG.'})
        
        
        
        # Change the image names to with the user's id
        self.drivers_license_front.name = f'{self.user.id}_{self.drivers_license_front.name}'
        self.drivers_license_back.name = f'{self.user.id}_{self.drivers_license_back.name}'
        self.driver_selfie.name = f'{self.user.id}_{self.driver_selfie.name}'
        self.driver_photo.name = f'{self.user.id}_{self.driver_photo.name}'
        
        

    
    def __str__(self):
        return self.user.name

class DriverApplication(models.Model):
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, related_name='application')
    is_approved = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    can_reapply = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.driver.user.name