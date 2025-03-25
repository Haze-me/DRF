
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.models import User
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth import logout
# -----------------------
# HTML Views (Frontend)
# -----------------------

def home_view(request):
    return render(request, "webapp/home.html")

def login_view(request):
    """Renders the login page."""
    return render(request, "webapp/login.html")

def register_view(request):
    """Renders the registration page."""
    return render(request, "webapp/register.html")


def user_logout(request):
    logout(request)
    return redirect("home")  # Redirect to home after logout



@login_required
def dashboard(request):
    return render(request, "webapp/dashboard.html")

@login_required
def profile(request):
    if request.method == "POST":
        user = request.user
        user.username = request.POST["username"]
        user.email = request.POST["email"]

        if "profile_picture" in request.FILES:
            user.profile_picture = request.FILES["profile_picture"]

        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("profile")

    return render(request, "webapp/profile.html")


class CustomPasswordChangeView(PasswordChangeView):
    template_name = "webapp/password_change.html"
    success_url = reverse_lazy("password_change_done")

    def form_valid(self, form):
        messages.success(self.request, "Your password has been changed successfully!")
        return super().form_valid(form)
