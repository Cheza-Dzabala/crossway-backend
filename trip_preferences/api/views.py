from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializer import TripPreferencesSerializer
from trip_preferences.models import TripPreferences



class TripPreferencesAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        preferences = TripPreferences.objects.filter(is_active=True)
        serializedPreferences = TripPreferencesSerializer(preferences, many=True)
        return Response({
            'message': 'Trip preferences fetched successfully',
            'data': serializedPreferences.data
        }, status=200)