# Generated by Django 5.0.1 on 2024-02-05 22:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entidades', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TempMod',
        ),
        migrations.RemoveField(
            model_name='bannerprincipal',
            name='contenido',
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='color_boton',
            field=models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='color_de_fondo',
            field=models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='color_de_letra',
            field=models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='color_letra_boton',
            field=models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='descripcion',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='encabezado',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='enlace',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='foto',
            field=models.FileField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='seleccionar_acontecimiento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banner_principal', to='entidades.acontecimiento'),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='seleccionar_efemeride',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banner_principal', to='entidades.efemerides'),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='seleccionar_evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banner_principal', to='entidades.evento'),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='tipografia_descripcion',
            field=models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='tipografia_encabezado',
            field=models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='tipografia_enlace',
            field=models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='tipografia_titulo',
            field=models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='bannerprincipal',
            name='titulo',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
