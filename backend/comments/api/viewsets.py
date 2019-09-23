from rest_framework import viewsets
from comments.models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer