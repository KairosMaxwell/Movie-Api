from django.contrib.auth import get_user_model
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from movie_account.models import CustomUser
from rest_framework import serializers

from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password_confirmation')

    def validate(self, data):
        # Ensure passwords match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        # Remove password confirmation before creating the user
        validated_data.pop('password_confirmation')
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user





class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)  # Only for update and create

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

    def update(self, instance, validated_data):
        # Update password if provided
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)  # Hash the password if it's being updated
        return super().update(instance, validated_data)

    def create(self, validated_data):
        # Create a user and hash the password
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user





class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        # Authenticate the user using the provided credentials
        user = authenticate(email=email, password=password)
        if not user:
            raise AuthenticationFailed("Invalid credentials")

        # Generate token for the authenticated user
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return {
            'refresh': str(refresh),
            'access': access_token,
            'user': {
                'id': user.id,
                # 'email': user.email,
                # 'username': user.username
            }
        }






