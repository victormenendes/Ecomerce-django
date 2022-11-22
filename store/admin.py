from django.contrib import admin

from .models import Categoria, Produto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
        lista_display = ['nome', 'slug']
        campos_prepopulados = {'slug': ('nome',)}

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
        lista_display = ['titulo', 'autor', 'slug', 'preco', 'in_stock', 'is_active', 'criado', 'atualizado']
        lista_filter = ['in_stock', 'is_active']
        lista_editavel = ['preco', 'in_stock']
        campos_prepopulados = {'slug': ('titulo',)}


