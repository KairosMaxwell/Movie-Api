from django.contrib import admin

from movie_account.models import CustomUser
# from movie_account.usermanager import ModelAdmin

# Register your models here.

admin.site.register(CustomUser)

