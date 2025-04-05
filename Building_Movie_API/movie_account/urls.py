from rest_framework import routers
from django.urls import path ,include
from django.contrib.auth.views import LoginView,LogoutView
from . import views

urlpatterns = [
    path("login/",LoginView.as_view(template_name="./registration/login.html")),
    path("logout/",LogoutView.as_view()),
    # path("register/",views.SignUpView,name="register"),
    path("register/", views.SignupView.as_view())
]