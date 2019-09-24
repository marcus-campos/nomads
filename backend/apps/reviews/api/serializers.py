from rest_framework.serializers import ModelSerializer
from apps.reviews.models import Review


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'comment', 'rate', 'created_at']