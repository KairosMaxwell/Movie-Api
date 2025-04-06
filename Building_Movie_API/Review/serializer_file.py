


from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['Movie_title','Rating','created_Date','user']
        read_only_fields = ['user', 'created_Date']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def create(self, validated_data):
        # Automatically associate the review with the current logged-in user
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)





