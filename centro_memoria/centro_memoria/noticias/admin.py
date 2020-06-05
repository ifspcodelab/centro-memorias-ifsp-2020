from django.contrib import admin
from .models import Noticia, FotoNoticia

class NoticiaAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'descricao', 'destaque', 'criado_em', 'atualizado_em']
    search_fields = ['titulo', 'destaque', 'criado_em', 'atualizado_em']
    list_filter = ['titulo', 'destaque']

class FotoNoticiaAdmin(admin.ModelAdmin):

    list_display = ['noticia', 'destaque', 'criado_em', 'atualizado_em']
    search_fields = ['noticia', 'destaque', 'criado_em', 'atualizado_em']
    list_filter = ['noticia', 'destaque']


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(FotoNoticia, FotoNoticiaAdmin)