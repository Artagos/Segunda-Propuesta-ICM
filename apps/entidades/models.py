from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class ContenedorConFondo (models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    foto = models.FileField(upload_to='images/', max_length=100)

class ContenedorConFondoSoloTitulo (models.Model):
    titulo = models.CharField(max_length=50)
    foto = models.FileField(upload_to='images/', max_length=100)

class ContenedorICM (models.Model):
    titulo = models.CharField(max_length=50)
    encabezado = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    enlace = models.URLField(max_length=200)
    foto = models.FileField(upload_to='images/', max_length=100)
    color_de_fondo = models.CharField(max_length=7)
    color_de_letra = models.CharField(max_length=7)
    color_boton = models.CharField(max_length=7)
    color_letra_boton = models.CharField(max_length=7)

class ContenedorEfemeride (models.Model):
    color_de_fondo = models.CharField(max_length=7)


class BannerPrincipal(models.Model):
    CONTENEDOR_CHOICES = [
        ('ContenedorConFondo', 'Contenedor: Titulo + Descripcion + Foto'),
        ('ContenedorConFondoSoloTitulo', 'Contenedor: Titulo + Descripcion + Foto'),
        ('ContenedorICM', 'Contenedor: Titulo + Encabezado + Descripcion + Foto'),
        ('Evento', 'Contenedor: Evento'),
        ('Acontecimiento', 'Contenedor: Acontecimiento'),
        ('Efemeride', 'Contenedor: Efemeride'),
    ]



    tipo_contenedor = models.CharField(max_length=50, choices=CONTENEDOR_CHOICES)
    #posicion_en_pantalla = models.PositiveIntegerField(unique=True)
    seleccionar_efemeride = models.ForeignKey('Efemerides', on_delete=models.CASCADE, related_name='banner_principal', null=True)
    seleccionar_acontecimiento = models.ForeignKey('Acontecimiento', on_delete=models.CASCADE, related_name='banner_principal', null=True)
    seleccionar_evento = models.ForeignKey('Evento', on_delete=models.CASCADE, related_name='banner_principal', null=True)

    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]

    titulo = models.CharField(max_length=50, null=True)
    encabezado = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=500, null=True)
    enlace = models.URLField(max_length=200, null=True)
    foto = models.FileField(upload_to='images/', max_length=100, null=True)


    color_de_fondo = models.CharField(max_length=7, choices=TEXT_COLOR_CHOICES, null=True)
    color_de_letra = models.CharField(max_length=7, choices=TEXT_COLOR_CHOICES, null=True)
    color_boton = models.CharField(max_length=7, choices=TEXT_COLOR_CHOICES, null=True)
    color_letra_boton = models.CharField(max_length=7, choices=TEXT_COLOR_CHOICES, null=True)


    tipografia_titulo = models.CharField(max_length=50, choices=TEXT_TIPOGRAPHY_CHOICES, null=True)
    tipografia_encabezado = models.CharField(max_length=50, choices=TEXT_TIPOGRAPHY_CHOICES, null=True)
    tipografia_descripcion = models.CharField(max_length=50, choices=TEXT_TIPOGRAPHY_CHOICES, null=True)
    tipografia_enlace = models.CharField(max_length=50, choices=TEXT_TIPOGRAPHY_CHOICES, null=True)


    numero_unico = models.PositiveIntegerField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.tipo_contenedor

class Iconos (models.Model):
    ICON_CHOICES = [
        ('S_Efemerides', 'Sección Efemerides'),
        ('S_BannerPpal', 'Sección Banner Principal'),
        ('S_Eventos', 'Sección Eventos'),
        ('S_Revista', 'Sección Revista'),

    ]

    seccion = models.CharField(max_length=50, choices=ICON_CHOICES)
    foto = models.FileField(upload_to='images/', max_length=100, null=True)

    def __str__(self):
        return self.seccion



class Seccion_Efemerides (models.Model):

    seleccionar_efemeride = models.ForeignKey('Efemerides', on_delete=models.CASCADE, related_name='seccion_efemerides', null=True)
    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]
    color_de_fondo = models.CharField(max_length=7, choices=TEXT_COLOR_CHOICES, null=True)
    numero_unico = models.PositiveIntegerField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.seleccionar_efemeride.titulo


class Evento (models.Model):
    título = models.CharField(max_length=100, default='None')
    descripción = models.CharField(max_length=500)
    fecha = models.DateField()
    hora = models.TimeField()
    enlace = models.URLField(max_length=200)
    foto = models.FileField(upload_to='images/', max_length=100)
    mostrar_en_banner_principal = models.BooleanField()


    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]

    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    tipografía_de_título = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_título = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff')
    foto_de_fondo = models.FileField(upload_to='images/', max_length=100)


    def __str__(self):
        return self.título


class Historia_de_la_Institución (models.Model):
    class Meta:
        verbose_name_plural = "Historia_de_la_Institución"
    título = models.CharField(max_length=100, default='None')
    descripción = models.CharField(max_length=500)
    foto = models.FileField(upload_to='images/', max_length=100)
    tipografía = models.CharField(max_length=100)

    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]

    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    tipografía_de_título = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_título = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff')
    foto_de_fondo = models.FileField(upload_to='images/', max_length=100)



    def __str__(self):
        return self.título

class Centros_y_Empresas (models.Model):
    class Meta:
        verbose_name_plural = "Centros_y_Empresas"
    nombre = models.CharField(max_length=100, default='None')
    dirección = models.CharField(max_length=500)
    télefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100)

    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]

    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    tipografía_de_título = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_título = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff')
    foto_de_fondo = models.FileField(upload_to='images/', max_length=100)

    def __str__(self):
        return self.nombre

class Directores (models.Model):
    class Meta:
        verbose_name_plural = "Directores"
    nombre = models.CharField(max_length=100, default='None')
    cargo = models.CharField(max_length=100)
    télefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100)
    consejo_de_dirección = models.BooleanField()
    empresa = models.OneToOneField("Centros_y_Empresas", on_delete=models.CASCADE)

    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]

    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')


    def __str__(self):
        return self.nombre

class Premio_Nacional_de_Música (models.Model):
    class Meta:
        verbose_name_plural = "Premio_Nacional_de_Música"
    titulo = models.CharField(max_length=100, default='None')
    año = models.DateField()
    descripión = models.CharField(max_length=500)
    bibliografía = models.CharField(max_length=500)
    foto = models.FileField(upload_to='images/', max_length=100)


    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]

    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    # tipografía_de_título = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    # color_de_título = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff')
    foto_de_fondo = models.FileField(upload_to='images/', max_length=100)

    def __str__(self):
        return self.titulo

class Acontecimiento (models.Model):
    título = models.CharField(max_length=100, default='None')
    descripción = models.CharField(max_length=500)
    fecha_de_publicación = models.DateField()
    enlace = models.URLField(max_length=200)
    foto = models.FileField(upload_to='images/', max_length=100)
    mostrar_en_banner_principal = models.BooleanField()
    relevante = models.BooleanField()


    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]

    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    tipografía_de_título = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_título = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff')
    foto_de_fondo = models.FileField(upload_to='images/', max_length=100)


    def __str__(self):
        return self.título


class Multimedia (models.Model):
    nombre = models.CharField(max_length=100, default='None')
    descripción = models.CharField(max_length=500)
    tipo = models.CharField(max_length=100)
    enlace = models.URLField(max_length=200)
    foto = models.FileField(upload_to='images/', max_length=100)


    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]

    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    tipografía_de_título = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_título = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff')
    foto_de_fondo = models.FileField(upload_to='images/', max_length=100)

    def __str__(self):
        return self.nombre

class Efemerides (models.Model):
    class Meta:
        verbose_name_plural = "Efemérides"
    titulo = models.CharField(max_length=100, default='None')
    fecha = models.DateField()
    descripción = models.CharField(max_length=500)
    #foto = models.FileField(upload_to='images/', max_length=100)
   # premio_nacional_de_la_música = models.OneToOneField("Premio_Nacional_de_Música", on_delete=models.CASCADE)
    #enlace = models.URLField(max_length=200)
    mostrar_en_banner_principal = models.BooleanField()
    # relevante = models.BooleanField()


    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]

    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    tipografía_de_título = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_título = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff')
   # foto_de_fondo = models.FileField(upload_to='images/', max_length=100)


    def __str__(self):
        return self.titulo
