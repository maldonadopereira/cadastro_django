from django.contrib import admin

from clientes.models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade')
    list_display_links = ('nome',)