from rest_framework import serializers

from user.serializers import AccountSerializer
from . models import Rent_detail
from jobportal.serializer import CategorySerializer,CitySerializer,DistrictSerializer

class RentSerializer(serializers.ModelSerializer):
    user=AccountSerializer(many=False)
    category=CategorySerializer(many=False)
    district=DistrictSerializer(many=False)
    city=CitySerializer(many=False)
    booked_person=AccountSerializer(many=False)
    class Meta:
        model=Rent_detail
        fields='__all__'