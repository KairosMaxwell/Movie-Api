
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from movie_account.models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields =["id","username","password","email"]

    def create(self,**validated_data):
        user =CustomUser.objects.create_user(**validated_data)
        # user =CustomUser.objects.create_user(self.validated_data, email=self.validated_data["email"],password=self.validated_data["password"])
        # CustomUser.objects.create_user(email=email, password=password )
        Token.objects.create(user=user)
        return user




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email", "password")

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)