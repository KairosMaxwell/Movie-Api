from django.contrib.auth.models import AbstractUser

from movie_account.usermanager import CustomUserManager
from django.db import models

# Create your models here.



class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)

    objects = CustomUserManager()

    # profile_picture = models.ImageField(upload_to="profile_pictures", null=True, blank=True)














