from rest_framework.serializers import ModelSerializer
from users.models import User
from PIL import Image

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name', 'phone_number', 'email', 'role', 'avatar']
        
    def validate_avatar(self, value):
        try:
            Image.open(value).verify()
        except Exception:
            raise serializers.ValidationError("Invalid image file")
        return value