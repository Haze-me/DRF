
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    UserListView, UserDetailView, RegisterView, LogoutView, 
    UserProfileView
)

urlpatterns = [

    # API Endpoints
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("user/", UserProfileView.as_view(), name="user-profile"),
    path("register/", RegisterView.as_view(), name="api-register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),

    # JWT Authentication
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),  # Get access & refresh tokens
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),  # Refresh access token
]
