# Generated by Django 5.0.1 on 2024-02-06 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0002_delete_tempmod_remove_bannerprincipal_contenido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerprincipal',
            name='numero_unico',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
