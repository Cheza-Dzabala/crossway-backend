from rest_framework.serializers import ModelSerializer
from drivers.models import Driver

class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'id', 
            'user_id',
            'drivers_license_front',
            'drivers_license_back',
            'driver_selfie',
            'is_profile_complete',
            'is_active',
            'is_banned',
            'ban_reason'
            ]
        