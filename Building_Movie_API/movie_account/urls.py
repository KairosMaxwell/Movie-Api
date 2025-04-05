from django.contrib.auth.views import LoginView,LogoutView
from movie_account import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("login/",LoginView.as_view(template_name="./registration/login.html")),
    path("logout/",LogoutView.as_view()),
    # path("register/",views.SignUpView,name="register"),
    path("register/", views.SignupView.as_view())
]