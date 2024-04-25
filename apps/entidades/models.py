from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import fitz  # Importa PyMuPDF
from django.core.files.base import ContentFile
from ckeditor.fields import RichTextField

class Revista(models.Model):

    titulo = RichTextField(config_name = 'small', blank=False, null=False)
    descripcion = RichTextField(blank=False, null=False)
    pdf = models.FileField(upload_to='pdfs/',blank=False, null=False)
    imagen_portada = models.ImageField(upload_to='images/')

    def get_foto_url(self):
        if self.foto and hasattr(self.imagen_portada, 'url'):
            return 'https://back.dcubamusica.cult.cu/public/' + self.foto.url
        return None

    def get_pdf_url(self):
        if self.foto and hasattr(self.imagen_portada, 'url'):
            return 'https://back.dcubamusica.cult.cu/public/' + self.pdf.url
        return None

    def __str__(self):
        return str(self.titulo)

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
    titulo = RichTextField(config_name = 'small', blank=False, null=False)
    descripcion = RichTextField(blank=False, null=False)
    link_podcast = models.URLField(blank=False, null=False)  # Puede contener tanto URLs locales como externas
    foto = models.ImageField(upload_to='images/', null=True)

    def get_foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return 'https://back.dcubamusica.cult.cu/public/' + self.foto.url
        return None

    def __str__(self):
        return str(self.titulo)


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


class BannerPrincipal(models.Model):
    class Meta:
        verbose_name_plural = "Banner Principal"
    CONTENEDOR_CHOICES = [
        ('ContenedorConFondo', 'Tipo 1'),
        ('ContenedorConFondoSoloTitulo', 'Tipo 2'),
        ('ContenedorICM', 'Contenedor: Tipo 3'),
        ('Evento', 'Contenedor: Evento'),
        ('Acontecimiento', 'Contenedor: Acontecimiento'),
        ('Efemeride', 'Contenedor: Efemeride'),
    ]


    tipo_contenedor = models.CharField(max_length=50, choices=CONTENEDOR_CHOICES)
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
    titulo = RichTextField(config_name = 'small', blank=True, null=True)
    encabezado = RichTextField(config_name = 'small', blank=True, null=True)
    descripcion = RichTextField(blank=True, null=True)
    foto = models.FileField(upload_to='images/', null=True)

    def get_foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return 'https://back.dcubamusica.cult.cu/public/' + self.foto.url
        return None



    color_de_fondo = models.CharField(max_length=7, choices=TEXT_COLOR_CHOICES, null=True)
    numero_unico = models.PositiveIntegerField(unique=True, blank=False, null=False)

    def __str__(self):
        if self.seleccionar_efemeride and self.seleccionar_efemeride.titulo:
            return str(self.seleccionar_efemeride.titulo)
        elif self.seleccionar_acontecimiento and self.seleccionar_acontecimiento.titulo:
            return str(self.seleccionar_acontecimiento.titulo)
        elif self.seleccionar_evento and self.seleccionar_evento.titulo:
            return str(self.seleccionar_evento.titulo)
        else:
            return str(self.titulo)



class Iconos (models.Model):
    class Meta:
        verbose_name_plural = "Iconos"
    ICON_CHOICES = [
        ('S_Efemerides', 'Sección Efemerides'),
        ('S_BannerPpal', 'Sección Banner Principal'),
        ('S_Eventos', 'Sección Eventos'),
        ('S_Revista', 'Sección Revista'),

    ]

    seccion = models.CharField(max_length=50, choices=ICON_CHOICES, blank=False, null=False)
    foto = models.FileField(upload_to='logos/', blank=False, null=False)

    def get_foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return 'https://back.dcubamusica.cult.cu/public/' + self.foto.url
        return None

    def __str__(self):
        return self.seccion


class Evento (models.Model):
    class Meta:
        verbose_name_plural = "Eventos"

    titulo = RichTextField(config_name = 'small', blank=False, null=False)
    fecha = models.DateField()
    encabezado = RichTextField(blank=False, null=False)
    descripcion = RichTextField(blank=False, null=False)
    enlace = models.URLField(max_length=200,blank=False, null=False)
    hora = models.TimeField(blank=False, null=False)

    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff', null=True)
    foto = models.FileField(upload_to='images/', max_length=100, null=True)

    def get_foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return 'https://back.dcubamusica.cult.cu/public/' + self.foto.url


    def __str__(self):
        return str(self.titulo)


class Historia_de_la_Institución (models.Model):
    class Meta:
        verbose_name_plural = "Historia de la Institución"
    titulo = RichTextField(config_name = 'small', blank=False, null=False)
    descripcion = RichTextField(blank=False, null=False)
    foto = models.FileField(upload_to='images/', max_length=100,blank=True, null=True)

    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff', null=True)

    def get_foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return 'https://back.dcubamusica.cult.cu/public/' + self.foto.url



    def __str__(self):
        return str(self.titulo)

class Centros_y_Empresas (models.Model):
    class Meta:
        verbose_name_plural = "Centros y Empresas"
    nombre = RichTextField(config_name = 'small', blank=False, null=False)
    dirección = models.CharField(max_length=500,blank=False, null=False)
    télefono = models.CharField(max_length=20,blank=False, null=False)
    correo = models.EmailField(max_length=100,blank=False, null=False)

    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    def __str__(self):
        return str(self.nombre)

class Directores (models.Model):
    class Meta:
        verbose_name_plural = "Directores"
    nombre = RichTextField(config_name = 'small', blank=False, null=False)
    foto = models.FileField(upload_to='images/', max_length=100 , default='https://back.dcubamusica.cult.cu/public/images/blank.webp' ,null=True)
    cargo = models.CharField(max_length=100,blank=False, null=False)
    télefono = models.CharField(max_length=20,blank=False, null=False)
    correo = models.EmailField(max_length=100,blank=False, null=False)
    consejo_de_dirección = models.BooleanField(blank=False, null=False)
    empresa = models.OneToOneField("Centros_y_Empresas", on_delete=models.CASCADE,blank=False, null=False)


    def __str__(self):
        return str(self.nombre)

class Premio_Nacional_de_Música (models.Model):
    class Meta:
        verbose_name_plural = "Premio Nacional de Música"
    titulo = RichTextField(config_name = 'small', blank=False, null=False)
    año = models.DateField()
    descripcion = RichTextField(blank=False, null=False)
    bibliografía = RichTextField(config_name = 'small', blank=True, null=True)
    foto = models.FileField(upload_to='images/', max_length=100, blank=True, null=True)


    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff', null=True)

    def get_foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return 'https://back.dcubamusica.cult.cu/public/' + self.foto.url

    def __str__(self):
        return str(self.titulo)

class Acontecimiento (models.Model):
    class Meta:
        verbose_name_plural = "Acontecimientos"

    titulo = RichTextField(config_name = 'small', blank=False, null=False)
    fecha = models.DateField(blank=False, null=False)
    encabezado = RichTextField(blank=False, null=False)
    descripcion = RichTextField(blank=False, null=False)
    enlace = models.URLField(max_length=200, blank=False, null=False)

    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff', null=True)
    foto = models.FileField(upload_to='images/', max_length=100, blank=False, null=False)

    def get_foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return 'https://back.dcubamusica.cult.cu/public/' + self.foto.url

    def __str__(self):
        return str(self.titulo)


class Multimedia (models.Model):
    class Meta:
        verbose_name_plural = "Multimedias"
    nombre = RichTextField(config_name = 'small', blank=False, null=False)

    descripcion = RichTextField(blank=False, null=False)
    tipo = models.CharField(max_length=100)
    enlace = models.URLField(max_length=200,blank=False, null=False)
    foto = models.FileField(upload_to='images/', max_length=100,blank=True, null=True)

    def get_foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return 'https://back.dcubamusica.cult.cu/public/' + self.foto.url


    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]

    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff', null=True)

    def __str__(self):
        return str(self.nombre)

class Efemerides (models.Model):
    class Meta:
        verbose_name_plural = "Efemérides"
    titulo = RichTextField(config_name = 'small', blank=False, null=False)
    fecha = models.DateField()
    encabezado = RichTextField(blank=False, null=False)
    descripcion = RichTextField(blank=False, null=False)

    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff', null=True)
    foto = models.FileField(upload_to='images/', max_length=100, blank=True, null=True)

    def get_foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return 'https://back.dcubamusica.cult.cu/public/' + self.foto.url


    def __str__(self):
        return str(self.titulo)
