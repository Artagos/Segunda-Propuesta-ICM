# Generated by Django 5.0.1 on 2024-04-28 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0002_alter_bannerprincipal_tipo_contenedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premio_nacional_de_música',
            name='año',
            field=models.IntegerField(),
        ),
    ]
