from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# from movie_account.usermanager import CustomUserManager
from django.db import models

from movie_account.usermanager import ModelAdmin


# Create your models here.

    # profile_picture = models.ImageField(upload_to="profile_pictures", null=True, blank=True)
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ModelAdmin()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username













