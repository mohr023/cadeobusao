from django.db import models

class Linha(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class PosicaoBusao(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    data_hora_registro = models.DateTimeField(auto_now=True)
    linha = models.ForeignKey(Linha, related_name='posicoes', related_query_name="posicao")

    def __str__(self):
        return str(self.lat) + " " + str(self.lon)
