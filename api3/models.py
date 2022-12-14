from django.core.validators import MinValueValidator
from django.db import models


class Reserva(models.Model):
    codigo_da_reserva = models.PositiveIntegerField(auto_created=True)
    reserva_pertence_ao_anuncio = models.PositiveIntegerField()
    check_in = models.DateField()
    check_out = models.DateField()
    preco_total = models.DecimalField(max_digits=8, decimal_places=2)
    comentario = models.CharField(max_length=320)
    numero_de_hospedes = models.PositiveIntegerField()
    data_hora_de_criacao = models.DateTimeField(auto_now=True)
    data_hora_de_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codigo_da_reserva

    # def validate_check_in(check_in, check_out):
    #     if check_in > check_out:
    #         raise MinValueValidator((f'data de check-in é anterior ao check-out'),
    #                                 params={'value': Reserva}, )
