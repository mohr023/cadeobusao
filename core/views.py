from cadeobusao.core.models import PosicaoBusao, Linha
from cadeobusao.core.serializers import LinhaSerializer, PosicaoBusaoSerializer
from rest_framework import generics


class LinhasView(generics.ListCreateAPIView):
    queryset = Linha.objects.all()
    serializer_class = LinhaSerializer


class PosicoesView(generics.ListCreateAPIView):
    serializer_class = PosicaoBusaoSerializer

    def get_queryset(self):
        linha = self.request.query_params.get('codigoLinha', None)
        queryset = PosicaoBusao.objects.filter(linha=linha)
        return queryset
