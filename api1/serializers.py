from rest_framework import routers, serializers, viewsets
from .models import Imovel

class ImovelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Imovel
        fields = ['id', 'codigo_imovel', 'limite_de_hospedes', 'quantidade_toilet', 'pet_friendly']