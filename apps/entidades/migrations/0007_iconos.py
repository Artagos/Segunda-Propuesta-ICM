# Generated by Django 5.0.1 on 2024-03-07 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0006_seccion_efemerides'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iconos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion', models.CharField(choices=[('S_Efemerides', 'Sección Efemerides'), ('S_BannerPpal', 'Sección Banner Principal'), ('S_Eventos', 'Sección Eventos'), ('S_Revista', 'Sección Revista')], max_length=50)),
                ('foto', models.FileField(null=True, upload_to='logos/')),
            ],
        ),
    ]
