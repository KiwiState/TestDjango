# Generated by Django 3.2.4 on 2021-06-16 03:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_usuarios_artista'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(null=True, primary_key=True, serialize=False, verbose_name='Id Categoria')),
                ('nombreCategoria', models.CharField(max_length=60, null=True, verbose_name='Concepto')),
            ],
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='artista',
            field=models.BooleanField(null=True, verbose_name='artista'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='correo',
            field=models.EmailField(max_length=200, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='edad',
            field=models.IntegerField(null=True, verbose_name='edad'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='id',
            field=models.IntegerField(null=True, primary_key=True, serialize=False, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='nombre',
            field=models.CharField(max_length=128, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='sexo',
            field=models.CharField(max_length=6, null=True, verbose_name='Sexo'),
        ),
        migrations.CreateModel(
            name='Pintura',
            fields=[
                ('id_pintura', models.IntegerField(null=True, primary_key=True, serialize=False, verbose_name='Id Pintura')),
                ('titulo', models.CharField(max_length=200, null=True, verbose_name='titulo')),
                ('descripcion', models.CharField(max_length=500, null=True, verbose_name='descripcion')),
                ('fecha', models.DateField(null=True, verbose_name='fecha')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='', verbose_name='imagen')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
                ('id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Id')),
            ],
        ),
    ]
