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

class Review(models.Model):
    Movie_title = models.CharField(max_length=255)
    Review_Content = models.TextField()
    Rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_id')
    created_Date = models.DateField(default=now)


    # movie_title = models.CharField(max_length=255)
    # review_content = models.TextField()
    # rating = models.IntegerField()
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User
    # created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Movie_title} - {self.user.username}"




