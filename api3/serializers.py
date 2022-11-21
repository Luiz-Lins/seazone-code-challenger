from rest_framework import serializers

from api3.models import Reserva


class ReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserva
        fields = [
            'codigo_da_reserva',
            'reserva_pertence_ao_anuncio',
            'check_in',
            'check_out',
            'preco_total',
            'comentario',
            'numero_de_hospedes',
            'data_hora_de_criacao',
            'data_hora_de_atualizacao',

        ]
