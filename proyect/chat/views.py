from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserLoginSerializer, UserSerializer
from rest_framework import permissions, status
#from .validations import custom_validation, validate_usuario, validate_password

class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self , request):
        data= request.data 
        #assert validate_usuario(data)
        #assert validate_password(data)

class UserView(APIView):
    pass