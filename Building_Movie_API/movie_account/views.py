from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializer import RegisterSerializer, UserSerializer, LoginSerializer


# from .serializer import UserSerializer, RegisterSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requires authentication

    def perform_create(self, serializer):
        serializer.save()



class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViews(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
           return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class RegisterView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]


# class SignupView(CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')  # Redirect to login page after signup
#     # template_name = './registration/signup.html'





from django import forms
from django.contrib.auth.models import User

# class SignupForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#
#         if password != confirm_password:
#             self.add_error("confirm_password", "Passwords must match!")

from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View


# class SignUpView(View):
#     def get(self, request):
#         form = SignupForm()
#         return render(request, "./registration/signup.html", {"form": form})

    # def post(self, request):
    #     form = SignupForm(request.POST)
    #     # if form.is_valid():
    #     #     user = form.save(commit=False)
    #     #     user.set_password(form.cleaned_data["password"])  # Hash password
    #     #     user.save()
    #     #     login(request, user)  # Log the user in after signup
    #     #     return redirect("home")  # Redirect to homepage or dashboard
    #
    #     return render(request, "./registration/signup.html", {"form": form})






