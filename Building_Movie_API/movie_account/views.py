from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requires authentication

    def perform_create(self, serializer):
        serializer.save()





class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after signup
    template_name = './registration/signup.html'





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






