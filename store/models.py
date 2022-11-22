from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    nome = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='criador_produto')
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255, default='Admin')
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='imagens/')
    slug = models.SlugField(max_length=255)
    preco = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'produtos'
        ordering = ('-criado',)

    def __str__(self):
        return self.titulo
