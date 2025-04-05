from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.



class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)

    # profile_picture = models.ImageField(upload_to="profile_pictures", null=True, blank=True)














