# Generated by Django 4.1.3 on 2022-11-22 18:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(default='Admin', max_length=255)),
                ('descricao', models.TextField(blank=True)),
                ('imagem', models.ImageField(upload_to='imagens/')),
                ('slug', models.SlugField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=4)),
                ('in_stock', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('atualizado', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='produtos', to='store.categoria')),
                ('criado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criador_produto', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'produtos',
                'ordering': ('-criado',),
            },
        ),
    ]
