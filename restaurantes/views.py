from rest_framework import viewsets
from rest_framework import generics
from .serializers import *
from .models import *
from django_filters import rest_framework
from rest_framework import filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RestaurantesViewSet(viewsets.ModelViewSet):
    queryset = Restaurantes.objects.all()
    serializer_class = RestaurantesSerializer



class EnderecosViewSet(viewsets.ModelViewSet):
    queryset = Enderecos.objects.all()
    serializer_class = EnderecosSerializer


class ComentariosViewSet(viewsets.ModelViewSet):
    queryset = Comentarios.objects.all()
    serializer_class = ComentariosSerializer


class AvaliacoesViewSet(viewsets.ModelViewSet):
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacoesSerializer


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    filter_backends = (filters.SearchFilter,)
    #filterset_fields = ('nome', 'estado')
    #filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    #filterset_fields = ['nome', 'estado']
    #search_fields = ('nome', 'estado')
    #ordering_fields = ['nome', 'estado']

class RestauranteList(generics.ListAPIView):
    queryset = Restaurantes.objects.all()
    serializer_class = RestaurantesSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('nome', 'enderecos',)
    search_fields = ('nome', )
    ordering_fields = ('nome', )