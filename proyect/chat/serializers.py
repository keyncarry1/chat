from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import authenticate

class UserLoginSerializer(serializers.Serializer):
    usuario = serializers.CharField()
    contra = serializers.CharField()

    def check_user(self, clean_data):
        user=authenticate(username=clean_data['usuario'], password = clean_data['contra'])
        if not user:
            raise ValidationError('usuario no encotrado')
        return user
    
class UserSerializer(serializers.ModelSerializer):
    pass