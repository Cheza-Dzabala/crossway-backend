from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializer import RideSerializer
from vehicles.models import Vehicle
from trip_preferences.models import TripPreferences, RidePreference
from users.models import User
from drivers.models import Driver
from django.db.models import Q
from datetime import timedelta, datetime
from rides.models import Ride

class RidesAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        VEHICLE_ID = request.data.get('vehicle')
        PREFERENCES = request.data.get('preferences') 

        # Validate vehicle
        vehicle = Vehicle.objects.filter(id=VEHICLE_ID).first()
        if not vehicle:
            return Response({
                'message': 'Vehicle does not exist',
                'errors': {}
            }, status=404)
        
        user = request.user
        driver = Driver.objects.filter(user=user).first()
        
        def vehicle_is_driver(vehicle):
            return vehicle.driver == driver
        
        if not vehicle_is_driver(vehicle):
            return Response({
                'message': 'Vehicle does not belong to this driver.',
                'errors': {}
            }, status=404)
            
        # Extract ride times
        try:
            departure = datetime.fromisoformat(request.data.get('departure'))  # ISO format: "2024-11-22T14:00:00Z"
            estimated_duration_str = request.data.get('estimated_duration')  # "01:30:00"
            estimated_duration_parts = datetime.strptime(estimated_duration_str, "%H:%M:%S")
            estimated_duration = timedelta(
                hours=estimated_duration_parts.hour,
                minutes=estimated_duration_parts.minute,
                seconds=estimated_duration_parts.second
            )
            estimated_arrival = departure + estimated_duration
        except Exception as e:
            return Response({
                'message': 'Invalid time data',
                'errors': str(e)
            }, status=400)

        # Validate overlapping rides
        overlapping_ride = Ride.objects.filter(
            Q(vehicle=vehicle) &
            Q(is_active=True) &
            Q(departure__lte=estimated_arrival) &
            Q(estimated_arrival__gte=departure)
        ).exists()

        if overlapping_ride:
            return Response({
                'message': 'Another active ride with this vehicle already exists in the specified time range.',
                'errors': {}
            }, status=400)

        # Validate ride data
        serializer = RideSerializer(data=request.data)
        if serializer.is_valid():
            try:
                # Save the ride
                ride = serializer.save(vehicle=vehicle)

                # Process preferences
                if PREFERENCES:
                    for preference_id in PREFERENCES:
                        # Validate preference exists
                        preference = TripPreferences.objects.filter(id=preference_id, is_active=True).first()
                        if preference:
                            # Create a RidePreference entry
                            RidePreference.objects.create(ride=ride, preference=preference)

                return Response({
                    'message': 'Ride created successfully',
                    'data': serializer.data
                }, status=201)
            except Exception as e:
                return Response({
                    'message': 'Ride creation failed',
                    'errors': str(e)
                }, status=400)
        else:
            return Response({
                'message': 'Ride creation failed',
                'errors': serializer.errors
            }, status=400)