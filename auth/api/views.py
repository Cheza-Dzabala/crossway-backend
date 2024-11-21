from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view




from users.models import User
from .serializers import UserSerializer
from drivers.api.serializers import DriverSerializer

@api_view(['POST'])
def login(request):
    if 'phone_number' not in request.data:
        return Response({'message': 'Phone number is required'}, status=400)
    if 'password' not in request.data:
        return Response({'message': 'Password is required'}, status=400)
    
    phone_number = request.data['phone_number']
    password = request.data['password']
    
    user = User.objects.get(phone_number=phone_number)
    
    if not user.is_active:
        return Response({'message': 'Account is not active'}, status=400)
    
    if not user.check_password(password):
        return Response({'message': 'Invalid credentials'}, status=400)
    
    refresh = RefreshToken.for_user(user)
    token = str(refresh.access_token)
    
    driver_data = None
    if hasattr(user, 'driver') and user.driver is not None:
            serializedDriver = DriverSerializer(user.driver, many=False)
            driver_data = serializedDriver.data
    
    serializedUser = UserSerializer(user, many=False)
    
    return Response({'token': {
        'access': token,
        'refresh': str(refresh)
        },
                     'driver_data': driver_data,
                     'response': {
                         'user': serializedUser.data, 
                         'driver': driver_data
                         },
                     })
    
    
@api_view(['POST'])
def register(request):
        serializer = UserSerializer(data=request.data)
        if 'password' not in request.data:
            return Response({'message': 'Password is required'}, status=400)
        
        if 'passwordConfirmation' not in request.data:
            return Response({'message': 'Password confirmation is required'}, status=400)
            
        password = request.data['password']
        passwordConfirmation = request.data['passwordConfirmation']
     
        if password != passwordConfirmation:
            return Response({'message': 'Passwords do not match'}, status=400)
        
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(phone_number=request.data['phone_number'])
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)
            user.set_password(request.data['password'])
            user.save()
            return Response({'token': {
                'access': token,
                'refresh': str(refresh)
                }, 'user': serializer.data})
        return Response(serializer.errors, status=400)