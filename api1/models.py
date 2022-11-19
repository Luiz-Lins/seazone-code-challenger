from django.db import models

class Imovel(models.Model):
    codigo_imovel = models.PositiveIntegerField()
    limite_de_hospedes = models.PositiveIntegerField()
    quantidade_toilet = models.PositiveIntegerField()
    pet_friendly = models.BooleanField()

    def __str__(self):
        return self.codigo_imovel
