from django.contrib import admin

from vendas.models import Venda


@admin.register(Venda)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'user')
    list_display_links = ('id',)