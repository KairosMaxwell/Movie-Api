

from rest_framework import serializers

from movie_account.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author= serializers.ReadOnlyField(source ="review.user.username")
    class Meta:
        model = Review
        fields = ["Movie_title",'Review_Content','Rating','user','created_Date']
