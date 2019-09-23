from rest_framework import viewsets
from addresses.models import Address
from .serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Address.objects.all().order_by('-created_at')
    serializer_class = AddressSerializer