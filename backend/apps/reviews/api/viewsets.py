from rest_framework import viewsets
from apps.reviews.models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer