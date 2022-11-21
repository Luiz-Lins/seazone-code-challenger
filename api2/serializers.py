from rest_framework import routers, serializers, viewsets
from api2.models import Anuncio


class AnuncioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anuncio
        fields = [
            'id',
            'anuncio_pertence_ao_imovel',
            'plataforma_anuncio_publicado',
            'tx_da_plataforma',
            'data_hora_de_criacao',
            'data_hora_de_atualizacao'
        ]
