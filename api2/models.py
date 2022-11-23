from django.db import models


class Anuncio(models.Model):
    anuncio_pertence_ao_imovel = models.PositiveIntegerField()
    plataforma_anuncio_publicado = models.CharField(max_length=15)
    tx_da_plataforma = models.DecimalField(max_digits=4, decimal_places=2)
    data_hora_de_criacao = models.DateTimeField(auto_now=True)
    data_hora_de_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.anuncio_pertence_ao_imovel
