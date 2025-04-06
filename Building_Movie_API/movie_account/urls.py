from django.contrib.auth.views import LoginView,LogoutView
from movie_account import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework.response import Response
from rest_framework import status

class CustomErrorHandlingMixin:
    def handle_exception(self, exc):
        if isinstance(exc, ValueError):
            return Response({"error": str(exc)}, status=status.HTTP_400_BAD_REQUEST)
        return super().handle_exception(exc)


router = DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("login/",LoginView.as_view()),
    path("logout/",LogoutView.as_view()),
    # path("register/",views.SignUpView,name="register"),
    path("register/", views.RegisterView.as_view())
]