from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import UserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class LoginUserView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        if user:
            token = RefreshToken.for_user(user)
            return Response({'access': str(token.access_token), 'refresh': str(token)})
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
