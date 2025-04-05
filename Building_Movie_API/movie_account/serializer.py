
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from movie_account.models import CustomUser

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ["id", "username", "email", "password"]
#         extra_kwargs = {"password": {"write_only": True}}
#



#
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields =["id","username","password","email"]

    def create(self,**validated_data):
        user =CustomUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already taken.")
        return value




class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email", "password")

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)