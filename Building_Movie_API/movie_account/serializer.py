


from rest_framework import serializers
from rest_framework.authtoken.models import Token

from movie_account.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model = User
        fields =["id","username","password","email","profile_picture"]

    def createUser(self):
        user =User.objects.create(**self.validated_data)
        Token.objects.create(user=user)
        return user