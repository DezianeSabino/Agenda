from django.contrib import admin
from AgendaApp.models import Contato, Cidade, Telefone, Interesse

class Telefones(admin.StackedInline):
    model = Telefone
    extra = 1

class ContatoAdmin (admin.ModelAdmin):
    list_display = [ 'id', 'nome', 'apelido', 'DataNascimento']
    list_display_links = ['id', 'nome']
    list_filter = ['DataNascimento', 'cidade', 'estado']
    search_fields = ['nome', 'apelido']
    inlines = [Telefones]
    filter_horizontal = ['interesses']


# Register your models here.
admin.site.register(Contato, ContatoAdmin)
admin.site.register(Cidade)
admin.site.register(Telefone)
admin.site.register(Interesse)