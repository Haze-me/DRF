
from django.urls import path
from .views import UserListView, UserDetailView, RegisterView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('register/', RegisterView.as_view(), name='register'),
]

# means we are adding new URL patterns to an existing urlpatterns list.
urlpatterns += [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Get access & refresh tokens
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh access token
    path('logout/', LogoutView.as_view(), name='logout'),
]

