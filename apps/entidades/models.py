from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import fitz  # Importa PyMuPDF
from django.core.files.base import ContentFile
from ckeditor.fields import RichTextField

class Revista(models.Model):

    titulo = RichTextField(config_name = 'small', blank=True, null=True)
    descripcion = RichTextField(blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs/')
    imagen_portada = models.ImageField(upload_to='images/')

    # def __str__(self):
    #     return self.titulo

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.imagen_portada:
            pdf_documento = fitz.open(self.pdf.path)
            pagina = pdf_documento[0]
            pix = pagina.get_pixmap()
            imagen_bytes = pix.tobytes("png")
            self.imagen_portada.save(f"portada_{self.pk}.png", ContentFile(imagen_bytes), save=False)
            pdf_documento.close()
            super().save(*args, **kwargs)


class Podcast(models.Model):
    titulo = RichTextField(config_name = 'small', blank=True, null=True)
    descripcion = RichTextField(blank=True, null=True)
    link_podcast = models.URLField(max_length=1024)  # Puede contener tanto URLs locales como externas
    foto = models.ImageField(upload_to='images/', null=True)

    # def __str__(self):
    #     return self.titulo

    def es_link_local(self):
        # Esto verificará si el link del podcast es relativo (local) o absoluto (externo)
        return not (self.link_podcast.startswith('http://') or self.link_podcast.startswith('https://'))

# class ContenedorConFondo (models.Model):
#     titulo = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=500)
#     foto = models.FileField(upload_to='images/', max_length=100)

# class ContenedorConFondoSoloTitulo (models.Model):
#     titulo = models.CharField(max_length=50)
#     foto = models.FileField(upload_to='images/', max_length=100)

# class ContenedorICM (models.Model):
#     titulo = models.CharField(max_length=50)
#     encabezado = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=500)
#     enlace = models.URLField(max_length=200)
#     foto = models.FileField(upload_to='images/', max_length=100)
#     color_de_fondo = models.CharField(max_length=7)
#     color_de_letra = models.CharField(max_length=7)
#     color_boton = models.CharField(max_length=7)
#     color_letra_boton = models.CharField(max_length=7)

class ContenedorEfemeride (models.Model):
    color_de_fondo = models.CharField(max_length=7)


class BannerPrincipal(models.Model):
    class Meta:
        verbose_name_plural = "Banner Principal"
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

    # TEXT_TIPOGRAPHY_CHOICES = [
    #     ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
    #     ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
    #     ('Montserrat Medium', 'Montserrat Medium'),
    #     ('Montserrat Regular','Montserrat Regular'),
    #     ('Montserrat Italic', 'Montserrat Italic'),
    # ]

    titulo = RichTextField(config_name = 'small', blank=True, null=True)
    encabezado = RichTextField(config_name = 'small', blank=True, null=True)
    descripcion = RichTextField(blank=True, null=True)
    enlace = models.URLField(max_length=200, null=True)
    foto = models.FileField(upload_to='images/', max_length=100, null=True)


    color_de_fondo = models.CharField(max_length=7, choices=TEXT_COLOR_CHOICES, null=True)
    # color_de_letra = models.CharField(max_length=7, choices=TEXT_COLOR_CHOICES, null=True)
    # color_boton = models.CharField(max_length=7, choices=TEXT_COLOR_CHOICES, null=True)
    # color_letra_boton = models.CharField(max_length=7, choices=TEXT_COLOR_CHOICES, null=True)


    # tipografia_titulo = models.CharField(max_length=50, choices=TEXT_TIPOGRAPHY_CHOICES, null=True)
    # tipografia_encabezado = models.CharField(max_length=50, choices=TEXT_TIPOGRAPHY_CHOICES, null=True)
    # tipografia_descripcion = models.CharField(max_length=50, choices=TEXT_TIPOGRAPHY_CHOICES, null=True)
    # tipografia_enlace = models.CharField(max_length=50, choices=TEXT_TIPOGRAPHY_CHOICES, null=True)


    numero_unico = models.PositiveIntegerField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.tipo_contenedor

class Iconos (models.Model):
    class Meta:
        verbose_name_plural = "Iconos"
    ICON_CHOICES = [
        ('S_Efemerides', 'Sección Efemerides'),
        ('S_BannerPpal', 'Sección Banner Principal'),
        ('S_Eventos', 'Sección Eventos'),
        ('S_Revista', 'Sección Revista'),

    ]

    seccion = models.CharField(max_length=50, choices=ICON_CHOICES)
    foto = models.FileField(upload_to='logos/', max_length=1000, null=True)

    def __str__(self):
        return self.seccion



class Seccion_Efemerides (models.Model):
    class Meta:
        verbose_name_plural = "Seccion Efemerides"
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
    class Meta:
        verbose_name_plural = "Eventos"
    titulo = RichTextField(config_name = 'small', blank=True, null=True)
    descripcion = RichTextField(blank=True, null=True)
    fecha = models.DateField()
    hora = models.TimeField()
    enlace = models.URLField(max_length=200)
    foto = models.FileField(upload_to='images/', max_length=100,null=True)
    # mostrar_en_banner_principal = models.BooleanField()


    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    # TEXT_TIPOGRAPHY_CHOICES = [
    #     ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
    #     ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
    #     ('Montserrat Medium', 'Montserrat Medium'),
    #     ('Montserrat Regular','Montserrat Regular'),
    #     ('Montserrat Italic', 'Montserrat Italic'),
    # ]

    # tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    # tipografía_de_titulo = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    # color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    # color_de_titulo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff', null=True)
    foto_de_fondo = models.FileField(upload_to='images/', max_length=100, null=True)


    def __str__(self):
        return self.titulo


class Historia_de_la_Institución (models.Model):
    class Meta:
        verbose_name_plural = "Historia de la Institución"
    titulo = RichTextField(config_name = 'small', blank=True, null=True)
    descripcion = RichTextField(blank=True, null=True)
    foto = models.FileField(upload_to='images/', max_length=100)
    # tipografía = models.CharField(max_length=100)

    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    # TEXT_TIPOGRAPHY_CHOICES = [
    #     ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
    #     ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
    #     ('Montserrat Medium', 'Montserrat Medium'),
    #     ('Montserrat Regular','Montserrat Regular'),
    #     ('Montserrat Italic', 'Montserrat Italic'),
    # ]

    # tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    # tipografía_de_titulo = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    # color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    # color_de_titulo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff', null=True)
    foto_de_fondo = models.FileField(upload_to='images/', max_length=100, null=True)



    def __str__(self):
        return self.titulo

class Centros_y_Empresas (models.Model):
    class Meta:
        verbose_name_plural = "Centros y Empresas"
    nombre = RichTextField(config_name = 'small', blank=True, null=True)
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

    # TEXT_TIPOGRAPHY_CHOICES = [
    #     ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
    #     ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
    #     ('Montserrat Medium', 'Montserrat Medium'),
    #     ('Montserrat Regular','Montserrat Regular'),
    #     ('Montserrat Italic', 'Montserrat Italic'),
    # ]

    # tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    # tipografía_de_titulo = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    # color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    # color_de_titulo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff', null=True)
    foto_de_fondo = models.FileField(upload_to='images/', max_length=100, null=True)

    def __str__(self):
        return self.nombre

class Directores (models.Model):
    class Meta:
        verbose_name_plural = "Directores"
    nombre = RichTextField(config_name = 'small', blank=True, null=True)
    foto = models.FileField(upload_to='images/', max_length=100 , null=True)
    cargo = models.CharField(max_length=100)
    télefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100)
    consejo_de_dirección = models.BooleanField()
    empresa = models.OneToOneField("Centros_y_Empresas", on_delete=models.CASCADE)

    # TEXT_COLOR_CHOICES = [
    #     ('#000000', 'negro'),
    #     ('#ffffff','blanco'),
    #     ('#4f4f4f', 'gris'),
    #     ('#29385c', 'azul'),
    #     ('36454d', 'verde'),
    #     ('0d032b', 'malva'),
    #     ('ed8500', 'naranja'),
    # ]

    # TEXT_TIPOGRAPHY_CHOICES = [
    #     ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
    #     ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
    #     ('Montserrat Medium', 'Montserrat Medium'),
    #     ('Montserrat Regular','Montserrat Regular'),
    #     ('Montserrat Italic', 'Montserrat Italic'),
    # ]

    # tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    # color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')


    def __str__(self):
        return self.nombre

class Premio_Nacional_de_Música (models.Model):
    class Meta:
        verbose_name_plural = "Premio Nacional de Música"
    titulo = RichTextField(config_name = 'small', blank=True, null=True)
    año = models.DateField()
    descripcion = RichTextField(blank=True, null=True)
    bibliografía = models.CharField(max_length=500)
    foto = models.FileField(upload_to='images/', max_length=100, null=True)


    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    # TEXT_TIPOGRAPHY_CHOICES = [
    #     ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
    #     ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
    #     ('Montserrat Medium', 'Montserrat Medium'),
    #     ('Montserrat Regular','Montserrat Regular'),
    #     ('Montserrat Italic', 'Montserrat Italic'),
    # ]

    # tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    # tipografía_de_titulo = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    # color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    # color_de_titulo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff', null=True)
    foto_de_fondo = models.FileField(upload_to='images/', max_length=100, null=True)

    # def __str__(self):
    #     return self.titulo

class Acontecimiento (models.Model):
    class Meta:
        verbose_name_plural = "Acontecimientos"
    titulo = RichTextField(config_name = 'small', blank=True, null=True)
    descripcion = RichTextField(blank=True, null=True)
    fecha_de_publicación = models.DateField()
    enlace = models.URLField(max_length=200)
    foto = models.FileField(upload_to='images/', max_length=100)
    # mostrar_en_banner_principal = models.BooleanField()
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

    # TEXT_TIPOGRAPHY_CHOICES = [
    #     ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
    #     ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
    #     ('Montserrat Medium', 'Montserrat Medium'),
    #     ('Montserrat Regular','Montserrat Regular'),
    #     ('Montserrat Italic', 'Montserrat Italic'),
    # ]

    # tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    # tipografía_de_titulo = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    # color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    # color_de_titulo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff', null=True)
    foto_de_fondo = models.FileField(upload_to='images/', max_length=100, null=True)


    def __str__(self):
        return self.titulo


class Multimedia (models.Model):
    class Meta:
        verbose_name_plural = "Multimedias"
    nombre = RichTextField(config_name = 'small', blank=True, null=True)

    descripcion = RichTextField(blank=True, null=True)
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

    # TEXT_TIPOGRAPHY_CHOICES = [
    #     ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
    #     ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
    #     ('Montserrat Medium', 'Montserrat Medium'),
    #     ('Montserrat Regular','Montserrat Regular'),
    #     ('Montserrat Italic', 'Montserrat Italic'),
    # ]

    # tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    # tipografía_de_titulo = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    # color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    # color_de_titulo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff', null=True)
    foto_de_fondo = models.FileField(upload_to='images/', max_length=100, null=True)

    def __str__(self):
        return self.nombre

class Efemerides (models.Model):
    class Meta:
        verbose_name_plural = "Efemérides"
    titulo = RichTextField(config_name = 'small', blank=True, null=True)
    fecha = models.DateField()
    descripcion = RichTextField(blank=True, null=True)
    #foto = models.FileField(upload_to='images/', max_length=100)
   # premio_nacional_de_la_música = models.OneToOneField("Premio_Nacional_de_Música", on_delete=models.CASCADE)
    #enlace = models.URLField(max_length=200)
    # mostrar_en_banner_principal = models.BooleanField()
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

    # TEXT_TIPOGRAPHY_CHOICES = [
    #     ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
    #     ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
    #     ('Montserrat Medium', 'Montserrat Medium'),
    #     ('Montserrat Regular','Montserrat Regular'),
    #     ('Montserrat Italic', 'Montserrat Italic'),
    # ]

    # tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    # tipografía_de_titulo = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    # color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    # color_de_titulo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff', null=True)
   # foto_de_fondo = models.FileField(upload_to='images/', max_length=100, null=True)


    # def __str__(self):
    #     return self.titulo
