from django.contrib import admin
from .models import Generos, Filme
from rest_framework.authtoken.models import Token


@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
   list_display = ['nome']      
   search_fields = ['nome']     


@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
   list_display = ['titulo', 'descricao', 'ano_lancamento', 'genero', 'duracao']  
   search_fields = ['titulo', 'descricao']                            
   list_filter = ['ano_lancamento', 'genero', 'duracao']                                

admin.site.register(Token)
