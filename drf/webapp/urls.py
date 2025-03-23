
# from django.urls import path
# from django.shortcuts import render

# urlpatterns = [
#     path('register/', lambda request: render(request, 'webapp/register.html'), name='register'),
#     path('login/', lambda request: render(request, 'webapp/login.html'), name='login'),
# ]

from django.urls import path
from .views import home, dashboard, profile, CustomPasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
urlpatterns = [
    
    path("", home, name="home"),    # Home page
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="webapp/password_change_done.html"), name='password_change_done'),
]
