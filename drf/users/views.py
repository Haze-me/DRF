

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from .models import User
from .serializers import UserSerializer, RegisterSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



# Get custom user model
User = get_user_model()

# -----------------------
# API Views (Backend)
# -----------------------

class UserProfileView(APIView):
    """Returns authenticated user's profile details."""
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "profile_picture": user.profile_picture.url if user.profile_picture else None
        })


class UserListView(generics.ListAPIView):
    """Lists all users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """Shows details of a specific user."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


@method_decorator(csrf_exempt, name="dispatch")
class RegisterView(generics.CreateAPIView):
    """Handles user registration."""
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



@method_decorator(csrf_exempt, name="dispatch")
class LogoutView(APIView):
    """Handles user logout."""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response({"message": "Logged out successfully"}, status=200)
        response.delete_cookie('jwt')  # Remove JWT cookie
        return response
