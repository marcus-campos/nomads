from rest_framework import viewsets
from facilities.models import Facility
from .serializers import FacilitySerializer


class FacilityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Facility.objects.all().order_by('-created_at')
    serializer_class = FacilitySerializer