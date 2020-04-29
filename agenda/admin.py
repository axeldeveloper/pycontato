# Register your models here.

from django.contrib import admin

from .models import Contato




class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'url')
    search_fields = ['nome', 'telefone']
    ordering = ['-nome']
    list_filter = ['nome']
    date_hierarchy = 'data_criacao'


#registrando Modelo de Contao
admin.site.register(Contato, ContatoAdmin)