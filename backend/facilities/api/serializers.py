from rest_framework.serializers import ModelSerializer
from facilities.models import Facility


class FacilitySerializer(ModelSerializer):
    class Meta:
        model = Facility
        fields = ['id', 'name']