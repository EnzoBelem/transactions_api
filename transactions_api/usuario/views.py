from rest_framework import viewsets
from usuario.models import PessoaFisica, PessoaJuridica
from usuario.serializers import PessoaFisicaSerializer, PessoaJuridicaSerializer


class PessoaFisicaModelViewSet(viewsets.ModelViewSet):

    queryset = PessoaFisica.objects.all()
    serializer_class = PessoaFisicaSerializer


class PessoaJuridicaModelViewSet(viewsets.ModelViewSet):

    queryset = PessoaJuridica.objects.all()
    serializer_class = PessoaJuridicaSerializer