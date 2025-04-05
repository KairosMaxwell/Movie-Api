


from rest_framework import serializers
from .models import Review

# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = ['id', 'movie_title', 'review_content', 'rating', 'user', 'created_at']
#         read_only_fields = ['user', 'created_at']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'Movie_title','Rating','created_Date','user']
        read_only_fields = ['user', 'created_Date']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value



















from rest_framework import serializers

# from movie_account.models import Review

#
# class ReviewSerializer(serializers.ModelSerializer):
#     author= serializers.ReadOnlyField(source ="review.user.username")
#     class Meta:
#         model = Review
#         fields = ["Movie_title",'Review_Content','Rating','user','created_Date']
