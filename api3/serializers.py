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

class Check_in_out(serializers.Serializer):
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        return data
