from django.db import transaction
from rest_framework import serializers
from usuario.models import *
from usuario.utils import validar_cpf, validar_cnpj


class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endereco
        fields = '__all__'


class PessoaFisicaSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()

    class Meta:
        model = PessoaFisica
        fields = '__all__'

    def validate_cpf(self, cpf):
        try:
            return validar_cpf(cpf)
        except ValueError as e:
            raise serializers.ValidationError(e)
    
    @transaction.atomic
    def create(self, validated_data):
        endereco = Endereco.objects.create(**validated_data.pop('endereco'))
        return PessoaFisica.objects.create(**validated_data, endereco=endereco)


class PessoaJuridicaSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer()

    class Meta:
        model = PessoaJuridica
        fields = '__all__'

    def validate_cnpj(self, cnpj):
        try:
            return validar_cnpj(cnpj)
        except ValueError as e:
            raise serializers.ValidationError(e)
    
    @transaction.atomic
    def create(self, validated_data):
        endereco = Endereco.objects.create(**validated_data.pop('endereco'))
        return PessoaJuridica.objects.create(**validated_data, endereco=endereco)

