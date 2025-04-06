# from django.contrib.auth import User

from django.db import models

from movie_account.models import CustomUser

# Create your models here.

# class Review(models.Model):
#     Movie_title = models.CharField(max_length=255)
#     Review_Content = models.TextField()
#     Rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_id')
#     created_Date = models.DateField(auto_now=True)
#
#
#     def __str__(self):
#         return self.Movie_title


from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timezone import now
User = get_user_model()


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Review(models.Model):
    Movie_title = models.CharField(max_length=255)
    Review_Content = models.TextField()
    Rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_id')
    created_Date = models.DateField(default=now)




    def __str__(self):
        return f"{self.Movie_title} - {self.user.username}"




