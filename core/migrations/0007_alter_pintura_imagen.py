# Generated by Django 3.2.4 on 2021-06-22 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pintura',
            name='imagen',
            field=models.ImageField(null=True, upload_to='img/%y'),
        ),
    ]
