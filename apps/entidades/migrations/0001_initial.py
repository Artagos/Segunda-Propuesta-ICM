# Generated by Django 5.0.1 on 2024-02-05 21:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acontecimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(default='None', max_length=100)),
                ('descripción', models.CharField(max_length=500)),
                ('fecha_de_publicación', models.DateField()),
                ('enlace', models.URLField()),
                ('foto', models.FileField(upload_to='images/')),
                ('mostrar_en_banner_principal', models.BooleanField()),
                ('relevante', models.BooleanField()),
                ('tipografía_de_letra', models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], default='Montserrat Medium', max_length=100)),
                ('tipografía_de_título', models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], default='Bw Darius DEMO Bold', max_length=100)),
                ('color_de_letra', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#000000', max_length=7)),
                ('color_de_título', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#000000', max_length=7)),
                ('color_de_fondo', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#ffffff', max_length=7)),
                ('foto_de_fondo', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Centros_y_Empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='None', max_length=100)),
                ('dirección', models.CharField(max_length=500)),
                ('télefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=100)),
                ('tipografía_de_letra', models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], default='Montserrat Medium', max_length=100)),
                ('tipografía_de_título', models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], default='Bw Darius DEMO Bold', max_length=100)),
                ('color_de_letra', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#000000', max_length=7)),
                ('color_de_título', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#000000', max_length=7)),
                ('color_de_fondo', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#ffffff', max_length=7)),
                ('foto_de_fondo', models.FileField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Centros_y_Empresas',
            },
        ),
        migrations.CreateModel(
            name='ContenedorConFondo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
                ('foto', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='ContenedorConFondoSoloTitulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('foto', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='ContenedorEfemeride',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color_de_fondo', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='ContenedorICM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('encabezado', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=500)),
                ('enlace', models.URLField()),
                ('foto', models.FileField(upload_to='images/')),
                ('color_de_fondo', models.CharField(max_length=7)),
                ('color_de_letra', models.CharField(max_length=7)),
                ('color_boton', models.CharField(max_length=7)),
                ('color_letra_boton', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Efemerides',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='None', max_length=100)),
                ('fecha', models.DateField()),
                ('descripción', models.CharField(max_length=500)),
                ('mostrar_en_banner_principal', models.BooleanField()),
                ('tipografía_de_letra', models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], default='Montserrat Medium', max_length=100)),
                ('tipografía_de_título', models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], default='Bw Darius DEMO Bold', max_length=100)),
                ('color_de_letra', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#000000', max_length=7)),
                ('color_de_título', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#000000', max_length=7)),
                ('color_de_fondo', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#ffffff', max_length=7)),
            ],
            options={
                'verbose_name_plural': 'Efemérides',
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(default='None', max_length=100)),
                ('descripción', models.CharField(max_length=500)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('enlace', models.URLField()),
                ('foto', models.FileField(upload_to='images/')),
                ('mostrar_en_banner_principal', models.BooleanField()),
                ('tipografía_de_letra', models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], default='Montserrat Medium', max_length=100)),
                ('tipografía_de_título', models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], default='Bw Darius DEMO Bold', max_length=100)),
                ('color_de_letra', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#000000', max_length=7)),
                ('color_de_título', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#000000', max_length=7)),
                ('color_de_fondo', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#ffffff', max_length=7)),
                ('foto_de_fondo', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Historia_de_la_Institución',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('título', models.CharField(default='None', max_length=100)),
                ('descripción', models.CharField(max_length=500)),
                ('foto', models.FileField(upload_to='images/')),
                ('tipografía', models.CharField(max_length=100)),
                ('tipografía_de_letra', models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], default='Montserrat Medium', max_length=100)),
                ('tipografía_de_título', models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], default='Bw Darius DEMO Bold', max_length=100)),
                ('color_de_letra', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#000000', max_length=7)),
                ('color_de_título', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#000000', max_length=7)),
                ('color_de_fondo', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#ffffff', max_length=7)),
                ('foto_de_fondo', models.FileField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Historia_de_la_Institución',
            },
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='None', max_length=100)),
                ('descripción', models.CharField(max_length=500)),
                ('tipo', models.CharField(max_length=100)),
                ('enlace', models.URLField()),
                ('foto', models.FileField(upload_to='images/')),
                ('tipografía_de_letra', models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], default='Montserrat Medium', max_length=100)),
                ('tipografía_de_título', models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], default='Bw Darius DEMO Bold', max_length=100)),
                ('color_de_letra', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#000000', max_length=7)),
                ('color_de_título', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#000000', max_length=7)),
                ('color_de_fondo', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#ffffff', max_length=7)),
                ('foto_de_fondo', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Premio_Nacional_de_Música',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='None', max_length=100)),
                ('año', models.DateField()),
                ('descripión', models.CharField(max_length=500)),
                ('bibliografía', models.CharField(max_length=500)),
                ('foto', models.FileField(upload_to='images/')),
                ('tipografía_de_letra', models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], default='Montserrat Medium', max_length=100)),
                ('color_de_letra', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#000000', max_length=7)),
                ('color_de_fondo', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#ffffff', max_length=7)),
                ('foto_de_fondo', models.FileField(upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'Premio_Nacional_de_Música',
            },
        ),
        migrations.CreateModel(
            name='TempMod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Directores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='None', max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('télefono', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=100)),
                ('consejo_de_dirección', models.BooleanField()),
                ('tipografía_de_letra', models.CharField(choices=[('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'), ('Bw Darius DEMO Regular', 'Bw Darius DEMO Regular'), ('Montserrat Medium', 'Montserrat Medium'), ('Montserrat Regular', 'Montserrat Regular'), ('Montserrat Italic', 'Montserrat Italic')], default='Montserrat Medium', max_length=100)),
                ('color_de_letra', models.CharField(choices=[('#000000', 'negro'), ('#ffffff', 'blanco'), ('#4f4f4f', 'gris'), ('#29385c', 'azul'), ('36454d', 'verde'), ('0d032b', 'malva'), ('ed8500', 'naranja')], default='#000000', max_length=7)),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='entidades.centros_y_empresas')),
            ],
            options={
                'verbose_name_plural': 'Directores',
            },
        ),
        migrations.CreateModel(
            name='BannerPrincipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_contenedor', models.CharField(choices=[('ContenedorConFondo', 'Contenedor: Titulo + Descripcion + Foto'), ('ContenedorConFondoSoloTitulo', 'Contenedor: Titulo + Descripcion + Foto'), ('ContenedorICM', 'Contenedor: Titulo + Encabezado + Descripcion + Foto'), ('Evento', 'Contenedor: Evento'), ('Acontecimiento', 'Contenedor: Acontecimiento'), ('Efemeride', 'Contenedor: Efemeride')], max_length=50)),
                ('contenido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='banner_principal', to='entidades.efemerides')),
            ],
        ),
    ]