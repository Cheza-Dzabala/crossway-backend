from rest_framework.serializers import ModelSerializer
from drivers.models import Driver
from vehicles.api.serializer import VehicleSerializer

class DriverSerializer(ModelSerializer):
    vehicles = VehicleSerializer(many=True, read_only=True)
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
            'ban_reason',
            'vehicles',
            ]
        