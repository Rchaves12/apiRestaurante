from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'restaurantes', RestaurantesViewSet)
router.register(r'endereco', EnderecosViewSet)
router.register(r'comentario', ComentariosViewSet)
router.register(r'avaliacoes', AvaliacoesViewSet)
router.register(r'estado', EstadoViewSet)
router.register(r'cidade', CidadeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('restaurantefilter/', RestauranteList.as_view()),

]
