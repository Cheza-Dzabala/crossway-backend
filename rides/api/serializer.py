from rest_framework.serializers import ModelSerializer
from rides.models import Ride
from trip_preferences.models import TripPreferences
from trip_preferences.api.serializer import RidePreferenceSerializer

class RideSerializer(ModelSerializer):
    preferences = RidePreferenceSerializer(many=True, read_only=True)
    class Meta:
        model = Ride
        fields = [
            'id', 
            'estimated_duration',
            'estimated_arrival',
            'departure',
            'departure_location',
            'arrival_location',
            'preferences',
            'capacity',
        	]