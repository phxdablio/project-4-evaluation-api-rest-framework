from rest_framework import serializers  
from .models import Generos, Filme       

class GenerosSerializer(serializers.ModelSerializer):
   class Meta:
       model = Generos
       fields = '__all__'  

class FilmeSerializer(serializers.ModelSerializer):
   class Meta:
       model = Filme
       fields = '__all__'  