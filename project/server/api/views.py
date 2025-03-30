from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt
from django.conf import settings
from datetime import datetime, timedelta
from rest_framework import status
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FarmerProfileViewSet(viewsets.ModelViewSet):
    queryset = FarmerProfile.objects.all()
    serializer_class = FarmerProfileSerializer

@api_view(["POST"])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({"message": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)
        if not user.check_password(password):
            return Response({"message": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)
        
        # ✅ Generate JWT Token
        payload = {
            "user_id": user.user_id,
            "email": user.email,
            "role": user.role,
            "exp": datetime.utcnow() + timedelta(days=1),  # Token expiry
            "iat": datetime.utcnow(),
        }
        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")

        return Response({
            "message": "Login successful", 
            "token": token, 
            "user": {
                "user_id": user.user_id,
                "full_name": user.full_name,
                "email": user.email,
                "role": user.role,
            }
        }, status=status.HTTP_200_OK)
    
    except User.DoesNotExist:
        return Response({"message": "Invalid email or password"}, status=status.HTTP_401_UNAUTHORIZED)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            pass
        
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
