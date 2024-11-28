from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drivers.models import Driver
from .serializers import DriverSerializer
from users.models import User


class DriverApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        driver = Driver.objects.filter(user=user).first()
        if not driver:
            return Response({
                'message': 'User does not have a driver record',
                'data': {}
            }, status=404)
            
        serializedDriver = DriverSerializer(driver, many=False)
        return Response({
            'message': 'Driver profile fetched successfully',
            'data': serializedDriver.data 
        }, status=200)

    def post(self, request):
        # Ensure the logged-in user is used
        user = request.user

        # Add user to request data since the serializer will expect it
        request_data = request.data.copy()
        request_data['user_id'] = user.id
        
        # Set the user role to driver
        user.role = 'driver'
        

        
    
        # Use the serializer for validation and saving
        serializer = DriverSerializer(data=request_data)
            # Check if user exists on drivers table
        driver = Driver.objects.filter(user=user)
        if driver.exists():
                return Response({
                    'message': 'User already has driver profile',
                    'errors': {}
                }, status=400)
        
        if serializer.is_valid():
            try:
                driver = serializer.save(user=user)
                return Response({
                    'message': 'Driver created successfully',
                    'data': serializer.data
                }, status=201)
            except Exception as e:
                return Response({
                    'message': 'Driver creation failed',
                    'errors':f"An exception of type {e.__class__.__name__} occurred. Message: {e}"
                }, status=400)
        else:
            return Response({
                'message': 'Driver creation failed',
                'errors': serializer.errors
            }, status=400)

            
    def patch(self, request):
        def check_null_fields(instance):
            null_fields = []
            for field in instance._meta.fields:
                field_value = getattr(instance, field.name)
                if field_value is None:
                    null_fields.append(field.name)
            return null_fields

        user = request.user
        driver = Driver.objects.filter(user=user).first()
        REQUEST_FILES = request.FILES 

        LICENSE_FRONT = REQUEST_FILES.get('drivers_license_front')
        LICENSE_BACK = REQUEST_FILES.get('drivers_license_back')
        SELFIE = REQUEST_FILES.get('driver_selfie')

        if not driver:
            return Response({
                'message': 'User does not have a driver record',
                'data': {}
            }, status=404)

        # Check if the request data is empty
        request_data = request.data.copy()
        if not request_data and not REQUEST_FILES:
            return Response({
                'message': 'Please select at least one field to update',
                'errors': {}
            }, status=400)

        # Update drivers_license_front
        if LICENSE_FRONT:
            if driver.drivers_license_front:
                driver.drivers_license_front.delete(save=False)  # Do not save immediately
            driver.drivers_license_front = LICENSE_FRONT

        # Update drivers_license_back
        if LICENSE_BACK:
            if driver.drivers_license_back:
                driver.drivers_license_back.delete(save=False)  # Do not save immediately
            driver.drivers_license_back = LICENSE_BACK

        # Update driver_selfie
        if SELFIE:
            if driver.driver_selfie:
                driver.driver_selfie.delete(save=False)  # Do not save immediately
            driver.driver_selfie = SELFIE

        # Check if the driver profile is complete
        null_fields = check_null_fields(driver)
        driver.is_profile_complete = len(null_fields) == 0

        # Save the updated instance
        driver.save()

        # Save other data using the serializer
        serializer = DriverSerializer(driver, data=request_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Driver profile updated successfully',
                'data': serializer.data
            }, status=200)
        else:
            return Response({
                'message': 'Driver profile update failed',
                'errors': serializer.errors
            }, status=400)
            
        