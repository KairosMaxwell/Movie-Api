from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db import models

class ModelAdmin(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)


        return user


    def create_superuser(self,username, email, password=None, **extra_fields):
        user = self.create_user(username, email, password)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return self.create_user(email, password, **extra_fields)



