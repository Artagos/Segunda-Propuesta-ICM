# Generated by Django 5.0.1 on 2024-05-05 00:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0027_alter_acontecimiento_foto_alter_bannerprincipal_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directores',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entidades.centros_y_empresas'),
        ),
    ]
