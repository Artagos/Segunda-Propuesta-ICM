# Generated by Django 5.0.1 on 2024-04-28 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0007_alter_revista_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revista',
            name='imagen_portada',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
