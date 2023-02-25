from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, LoginView
urlpatterns=[
    path('register', views.SignupView.as_view() , name="register"),
    path('login', views.UserLoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(next_page="/"), name="logout"),
]