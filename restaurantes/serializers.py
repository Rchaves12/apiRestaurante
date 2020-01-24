from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EnderecosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enderecos
        fields = ('bairro', 'enderecos', 'numero', 'complemento', 'cidade')
        extra_kwargs = {"bairro": {"error_messages": {"required": "O campo BAIRRO é obrigatório."}}}


class RestaurantesSerializer(serializers.ModelSerializer):
    enderecos = EnderecosSerializer(required=True)

    class Meta:
        model = Restaurantes
        fields = ['nome', 'foto', 'enderecos', 'telefone']

    def create(self, validated_data):
        enderecos_data = validated_data.pop('enderecos')
        enderecos = Enderecos.objects.create(**enderecos_data)
        restaurantes = Restaurantes.objects.create(enderecos=enderecos, **validated_data)
        return restaurantes
        #return Restaurantes.objects.create(**validated_data)

class ComentariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentarios
        exclude = ('data_hora_cadastro', 'ativo')


class AvaliacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacoes
        exclude = ('data_hora_cadastro', 'ativo')


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        exclude = ('data_hora_cadastro', 'ativo')


class CidadeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cidade
        exclude = ('data_hora_cadastro', 'ativo')