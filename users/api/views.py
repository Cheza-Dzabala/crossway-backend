from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication



from users.models import User
from .serializers import UserSerializer



class UsersAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serialized = UserSerializer(user, many=False)
        return Response({
            'message': 'User fetched successfully',
            'user': serialized.data
        })
        
    def patch(self, request):
        user = User.objects.get(id=request.user.id)
        if  request.data.get('name') is not None:
            user.name = request.data.get('name')
        if  request.data.get('role') is not None:
            user.role = request.data.get('role')
        if  request.data.get('avatar') is not None:
            if user.avatar:
                user.avatar.delete()
                user.avatar = None
                user.save()
            user.avatar = request.data.get('avatar')
        user.save()
        serialized = UserSerializer(user, many=False)
   
            
        return Response({
            'message': 'User updated successfully',
            'user': serialized.data
        }, status=200)
    
 
    
