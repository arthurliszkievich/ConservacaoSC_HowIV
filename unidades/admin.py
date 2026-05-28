from django.contrib import admin
from .models import Instituicao, Municipio, UnidadeConservacao, Comunicacao

# Registrando as tabelas para aparecerem no Painel
admin.site.register(Instituicao)
admin.site.register(Municipio)
admin.site.register(UnidadeConservacao)
admin.site.register(Comunicacao)
