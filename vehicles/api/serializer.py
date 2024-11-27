from rest_framework.serializers import ModelSerializer
from vehicles.models import Vehicle, VehicleImage

class VehicleImageSerializer(ModelSerializer):
    class Meta:
        model = VehicleImage
        fields = ['id', 'image', 'uploaded_at']
        
class VehicleSerializer(ModelSerializer):
    images = VehicleImageSerializer(many=True, read_only=True)
    class Meta:
        model = Vehicle
        fields = ['id',
                  'is_approved', 
                  'is_active', 
                  'created_at', 
                  'updated_at', 
                  'make', 
                  'model', 
                  'year', 
                  'color', 
                  'license_plate', 
                  'blue_book', 
                  "condition",
                  'capacity', 
                  'mileage_at_registration', 
                  'mileage_at_last_service',
                  'images'
                ]
        
