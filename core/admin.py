from django.contrib import admin

from core.models import Produto




@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'preco', 'quantidade')