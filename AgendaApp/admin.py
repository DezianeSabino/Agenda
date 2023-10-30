from django.contrib import admin
from AgendaApp.models import Contato

class ContatoAdmin (admin.ModelAdmin):
    list_display = [ 'id', 'nome', 'apelido', 'data_nascimento']
    list_filter = ['data_nsacimento', 'cidade', 'estado']


# Register your models here.
admin.site.register(Contato)