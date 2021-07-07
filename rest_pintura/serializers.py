from rest_framework import serializers
from core.models import Pintura

class PinturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pintura
        fields=['id_pintura','titulo','id','descripcion','categoria','fecha','imagen']


  