# Generated by Django 3.2.4 on 2021-06-16 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210615_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='artista',
            field=models.BooleanField(default=0, verbose_name='artista'),
        ),
    ]
