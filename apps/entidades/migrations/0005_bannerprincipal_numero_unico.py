# Generated by Django 5.0.1 on 2024-02-06 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0004_remove_bannerprincipal_numero_unico'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerprincipal',
            name='numero_unico',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
