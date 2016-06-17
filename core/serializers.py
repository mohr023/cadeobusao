from rest_framework import serializers
from cadeobusao.core.models import PosicaoBusao, Linha

class LinhaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linha
        fields = ('id', 'nome')


class PosicaoBusaoSerializer(serializers.ModelSerializer):
    linha = LinhaSerializer

    class Meta:
        model = PosicaoBusao
        fields = ('lat', 'lon', 'linha')
