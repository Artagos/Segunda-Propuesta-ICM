# Generated by Django 5.0.1 on 2024-04-28 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0008_alter_revista_imagen_portada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revista',
            name='imagen_portada',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
