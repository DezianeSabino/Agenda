from django.contrib import admin
from AgendaApp.models import Contato, Cidade, Telefone

class Telefones(admin.StackedInline):
    model = Telefone

class ContatoAdmin (admin.ModelAdmin):
    list_display = [ 'id', 'nome', 'apelido', 'DataNascimento']
    list_filter = ['DataNascimento', 'cidade', 'estado']
    search_fields = ['nome', 'apelido']
    inlines = [Telefones]


# Register your models here.
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Cidade)
admin.site.register(Telefone)