# from django.contrib.auth import User
from django.db import models

from movie_account.models import CustomUser

# Create your models here.

class Review(models.Model):
    Movie_title = models.CharField(max_length=255)
    Review_Content = models.TextField()
    Rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_id')
    created_Date = models.DateField(auto_now=True)


    def __str__(self):
        return self.Movie_title



