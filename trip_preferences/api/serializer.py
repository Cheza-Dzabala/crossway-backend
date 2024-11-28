from rest_framework.serializers import ModelSerializer
from trip_preferences.models import TripPreferences, RidePreference

class TripPreferencesSerializer(ModelSerializer):
    class Meta:
        model = TripPreferences
        
        fields = ['id', 'name', 'description', 'is_active']

class RidePreferenceSerializer(ModelSerializer):
    
    class Meta:
        model = RidePreference
        fields = ['id', 'ride', 'preference', 'created_at']