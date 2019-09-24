from rest_framework import viewsets
from apps.places.models import Place
from .serializers import PlaceSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Place.objects.all().order_by('-created_at')
    serializer_class = PlaceSerializer