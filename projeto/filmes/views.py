from .models import Filme, Generos
from .serializers import FilmeSerializer, GenerosSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

class GenerosViewSet(viewsets.ModelViewSet):
    queryset = Generos.objects.all()
    serializer_class = GenerosSerializer

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()        
    serializer_class = FilmeSerializer     
    filter_backends = [DjangoFilterBackend]  
    filterset_fields = ['titulo', 'descricao', 'ano_lancamento', 'genero', 'duracao']

