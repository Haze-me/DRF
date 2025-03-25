
# from django.urls import path
# from django.shortcuts import render

# urlpatterns = [
#     path('register/', lambda request: render(request, 'webapp/register.html'), name='register'),
#     path('login/', lambda request: render(request, 'webapp/login.html'), name='login'),
# ]

from django.urls import path
from .views import (home_view, dashboard, profile, CustomPasswordChangeView,
login_view, user_logout, register_view )
from django.contrib.auth.views import PasswordChangeDoneView
urlpatterns = [
    
     # Frontend Pages
    path("home/", home_view, name="home"),    # Home page
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="webapp/password_change_done.html"), name='password_change_done'),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", user_logout, name="logout"),
]
