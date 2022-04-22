from django.contrib import admin

from fornecedores.models import Fornecedor


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'criacao')
    list_display_links = ('nome',)