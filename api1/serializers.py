from rest_framework import serializers
from api1.models import Imovel


class ImovelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Imovel
        fields = [
            'id',
            'codigo_imovel',
            'limite_de_hospedes',
            'quantidade_toilet',
            'pet_friendly',
            'tx_de_limpeza',
            'data_de_ativacao',
            'data_hora_de_criacao',
            'data_hora_de_atualizacao',

        ]
