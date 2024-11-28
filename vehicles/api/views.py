from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drivers.models import Driver
from vehicles.models import Vehicle, VehicleImage
from .serializer import VehicleSerializer

class VehiclesAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        driver = Driver.objects.filter(user=request.user).first()
        if not driver:
            return Response({
                'message': 'User does not have a driver record',
                'errors': {}
            }, status=404)
            
        vehicles = Vehicle.objects.filter(driver=driver).all()
        vehicles_serializer = VehicleSerializer(vehicles, many=True)
        return Response({
            'message': 'Vehicle fetched successfully',
            'data': vehicles_serializer.data
        }, status=200)
    
    def post(self, request):
        driver = Driver.objects.filter(user=request.user).first()
        if not driver:
            return Response({
                'message': 'User does not have a driver record',
                'errors': {}
            }, status=404)
        
        # Validate the request data for the Vehicle
        vehicle_data = request.data.copy()
        vehicle_data['driver'] = driver.id  # Add the driver ID to the request data
        
        # check if the driver has a vehicle
        if Vehicle.objects.filter(driver=driver).exists():
            return Response({
                'message': 'Driver already has a vehicle',
                'errors': {}
            }, status=400)
        
        # Validate the images
        IMAGES = request.FILES.getlist('images')  # Ensure multiple images can be uploaded
        print('Image length:', len(IMAGES))
        if len(IMAGES) < 4:
            return Response({
                'message': 'At least four images are required',
                'errors': {}
            }, status=400)
        
        for image in IMAGES:
            if not image.name.endswith('.jpg') and not image.name.endswith('.png'):
                return Response({
                    'message': 'All images must be a JPG or PNG',
                    'errors': {}
                }, status=400)
        
        # Validate and save the vehicle
        vehicle_serializer = VehicleSerializer(data=vehicle_data)
        if vehicle_serializer.is_valid():
            try:
                # Save the vehicle
                vehicle = vehicle_serializer.save(driver=driver)

                # Save the images
                for image in IMAGES:
                    VehicleImage.objects.create(vehicle=vehicle, image=image)

                return Response({
                    'message': 'Vehicle created successfully',
                    'data': vehicle_serializer.data
                }, status=201)
            except Exception as e:
                return Response({
                    'message': 'Vehicle creation failed',
                    'errors': str(e)
                }, status=400)
        else:
            return Response({
                'message': 'Vehicle creation failed',
                'errors': vehicle_serializer.errors
            }, status=400)
            
