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

    def post(self, request):
        # Ensure the logged-in user is used
        user = request.user

        # Add user to request data since the serializer will expect it
        request_data = request.data.copy()
        request_data['user'] = user.id

        # Use the serializer for validation and saving
        serializer = DriverSerializer(data=request_data)

        if serializer.is_valid():
            serializer.save()  # Save the Driver instance
            return Response({
                'message': 'Driver created successfully',
                'data': serializer.data
            }, status=201)
        else:
            return Response({
                'message': 'Driver creation failed',
                'errors': serializer.errors
            }, status=400)