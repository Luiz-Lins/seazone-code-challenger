from django.db import models


class Imovel(models.Model):
    codigo_imovel = models.PositiveIntegerField()
    limite_de_hospedes = models.PositiveIntegerField()
    quantidade_toilet = models.PositiveIntegerField()
    pet_friendly = models.BooleanField()
    # tx_de_limpeza = models.DecimalField(max_digits=3, decimal_places=2)
    data_de_ativacao = models.DateField(auto_now=True)
    data_hora_de_criacao = models.DateTimeField(auto_now=True)
    data_hora_de_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.codigo_imovel
