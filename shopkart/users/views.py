from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView

from .form import CustomUserForm


# Create your views here.

class SignupView(CreateView):
    model = User
    form_class = CustomUserForm
    template_name = "users/register.html"
    success_url = "/users/login"


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True
    # success_message = "logged in successfully"
