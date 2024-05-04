from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import fitz  # Importa PyMuPDF
from django.core.files.base import ContentFile
from ckeditor.fields import RichTextField
from django.utils.translation import get_language
from django.core.files.storage import default_storage
from django.conf import settings
from django.utils.text import slugify
import os





class ImageManagementMixin(models.Model):
    """
    Mixin para manejar la verificación y reutilización de archivos de imágenes existentes.
    """
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Este método asume que el campo de la imagen se llama 'imagen_portada'
        if hasattr(self, 'foto') and self.foto:
            # Construye la ruta completa donde se guardaría la imagen
            self.foto.name = self.normalize_file_name(self.foto.name, 'images/')
            file_path = self.get_upload_path(self.foto.name)

            if default_storage.exists(file_path):

                self.foto = file_path
            else:

                super(ImageManagementMixin, self).save(*args, **kwargs)

        # Guarda la instancia del modelo
        super(ImageManagementMixin, self).save(*args, **kwargs)

    def normalize_file_name(self, filename, path):
        """
        Normalize and possibly clean up file names to match how Django would handle them on upload.
        """
        # You might want to further enhance this normalization
        base, ext = os.path.splitext(filename)
        return slugify(base) + ext.lower()

    def get_upload_path(self, filename):
        """
        Construye la ruta de carga basada en el directorio 'images/'
        """
        return os.path.join('images/', filename)


class Revista(models.Model):
    titulo = RichTextField(config_name='small', blank=False, null=False)
    descripcion = RichTextField(blank=False, null=False)
    fecha = models.DateField(blank=False, null=False)
    pdf = models.FileField(upload_to='pdfs/', blank=False, null=False,max_length=500)
    imagen_portada = models.ImageField(upload_to='images/',blank=False, null=False,max_length=500)

    def __str__(self):
        return str(self.titulo)

    def save(self, *args, **kwargs):
        self.imagen_portada.name = self.normalize_file_name(self.imagen_portada.name, 'images/')
        if self.imagen_portada and not self.imagen_portada_exists():
            super(Revista, self).save()
        else:
            self.imagen_portada = self.get_upload_path(self.imagen_portada.name, 'images/')  # Avoid saving the file again

        self.pdf.name = self.normalize_file_name(self.pdf.name, 'pdfs/')
        if self.pdf and not self.pdf_exists():
            super(Revista, self).save()
        else:
            self.pdf = self.get_upload_path(self.pdf.name, 'pdfs/')  # Avoid saving the file again

        # Always save the instance even if the files are not updated
        super(Revista, self).save(*args, **kwargs)

    def normalize_file_name(self, filename, path):
        """
        Normalize and possibly clean up file names to match how Django would handle them on upload.
        """
        # You might want to further enhance this normalization
        base, ext = os.path.splitext(filename)
        return slugify(base) + ext.lower()

    def imagen_portada_exists(self):
        return default_storage.exists(self.get_upload_path(self.imagen_portada.name, 'images/'))

    def pdf_exists(self):
        return default_storage.exists(self.get_upload_path(self.pdf.name, 'pdfs/'))

    def get_upload_path(self, filename, path):
        """
        Construct the full file path within the media directory
        """
        return os.path.join(path, filename)

    # def save(self, *args, **kwargs):
    #     if self.pk:
    #         original = Revista.objects.get(pk=self.pk)
    #         if original.pdf != self.pdf:  # Verifica si el PDF fue actualizado
    #             self.update_imagen_portada()
    #     else:
    #         self.update_imagen_portada()

    #     super().save(*args, **kwargs)

    # def update_imagen_portada(self):
    #     try:
    #         pdf_documento = fitz.open(self.pdf.path)  # Intenta abrir el PDF
    #         pagina = pdf_documento[0]  # Primera página
    #         pix = pagina.get_pixmap()
    #         imagen_bytes = pix.tobytes("png")
    #         self.imagen_portada.save(f"portada_{self.pk}.png", ContentFile(imagen_bytes), save=False)
    #     except Exception as e:
    #         print(f"Error al procesar el PDF: {e}")
    #     finally:
    #         pdf_documento.close()

    # def update_imagen_portada(self):
    # # Solo actualiza la imagen si no hay una existente
    #     if not self.imagen_portada:
    #         try:
    #             pdf_documento = fitz.open(self.pdf.path)
    #             pagina = pdf_documento[0]
    #             pix = pagina.get_pixmap()
    #             imagen_bytes = pix.tobytes("png")
    #             self.imagen_portada.save(f"portada_{self.pk}.png", ContentFile(imagen_bytes), save=False)
    #         except Exception as e:
    #             print(f"Error al procesar el PDF: {e}")
    #         finally:
    #             pdf_documento.close()




class Podcast(models.Model):
    titulo = RichTextField(config_name = 'small', blank=True, null=True)
    descripcion = RichTextField(blank=True, null=True)
    link_podcast = models.URLField(blank=True, null=True)  # Puede contener tanto URLs locales como externas
    archivo_local = models.FileField(upload_to='podcast/', blank=False, null=False,max_length=500)
    foto = models.ImageField(upload_to='images/',blank=False, null=False,max_length=500)

    def save(self, *args, **kwargs):
        # Check and set for image
        if self.foto:
            self.foto.name = self.normalize_file_name(self.foto.name, 'images/')
            if not self.file_exists(self.foto.name, 'images/'):
                super(Podcast, self).save()
            else:
                self.foto = self.get_upload_path(self.foto.name, 'images/')

        # Check and set for mp3
        if self.archivo_local:
            self.archivo_local.name = self.normalize_file_name(self.archivo_local.name, 'podcast/')
            if not self.file_exists(self.archivo_local.name, 'podcast/'):
                super(Podcast, self).save()
            else:
                self.archivo_local = self.get_upload_path(self.archivo_local.name, 'podcast/')

        # Always save the instance even if the files are not updated
        super(Podcast, self).save(*args, **kwargs)

    def file_exists(self, filename, path):
        full_path = self.get_upload_path(filename, path)
        return default_storage.exists(full_path)

    def get_upload_path(self, filename, path):
        return os.path.join(path, filename)

    def normalize_file_name(self, filename, path):
        """
        Normalize and possibly clean up file names to match how Django would handle them on upload.
        """
        # You might want to further enhance this normalization
        base, ext = os.path.splitext(filename)
        return slugify(base) + ext.lower()


    def __str__(self):
        return str(self.titulo)


# class ContenedorConFondo (models.Model):
#     titulo = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=500)
#     foto = models.FileField(upload_to='images/', max_length=500)

# class ContenedorConFondoSoloTitulo (models.Model):
#     titulo = models.CharField(max_length=50)
#     foto = models.FileField(upload_to='images/', max_length=500)

# class ContenedorICM (models.Model):
#     titulo = models.CharField(max_length=50)
#     encabezado = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=500)
#     enlace = models.URLField(max_length=200)
#     foto = models.FileField(upload_to='images/', max_length=500)
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
        ('ContenedorICM', 'Tipo 3'),
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
    foto = models.FileField(upload_to='images/', null=True, max_length=500)







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

    def save(self, *args, **kwargs):
        current_language = get_language()
        if self.seleccionar_efemeride:
            efemeride = self.seleccionar_efemeride
            if current_language == 'en':
                self.titulo_en = efemeride.titulo_en
                self.descripcion_en = efemeride.descripcion_en
                self.encabezado_en = efemeride.encabezado_en
            elif current_language == 'es':
                self.titulo_es = efemeride.titulo_es
                self.descripcion_es = efemeride.descripcion_es
                self.encabezado_es = efemeride.encabezado_es
            self.foto = efemeride.foto
            self.color_de_fondo = efemeride.color_de_fondo

        elif self.seleccionar_acontecimiento:
            acontecimiento = self.seleccionar_acontecimiento
            if current_language == 'en':
                self.titulo_en = acontecimiento.titulo_en
                self.descripcion_en = acontecimiento.descripcion_en
                self.encabezado_en = acontecimiento.encabezado_en
            elif current_language == 'es':
                self.titulo_es = acontecimiento.titulo_es
                self.descripcion_es = acontecimiento.descripcion_es
                self.encabezado_es = acontecimiento.encabezado_es
            self.foto = acontecimiento.foto
            self.color_de_fondo = acontecimiento.color_de_fondo

        elif self.seleccionar_evento:
            evento = self.seleccionar_evento
            if current_language == 'en':
                self.titulo_en = evento.titulo_en
                self.descripcion_en = evento.descripcion_en
                self.encabezado_en = evento.encabezado_en
            elif current_language == 'es':
                self.titulo_es = evento.titulo_es
                self.descripcion_es = evento.descripcion_es
                self.encabezado_es = evento.encabezado_es
            self.foto = evento.foto
            self.color_de_fondo = evento.color_de_fondo

        else:
            self.foto.name = self.normalize_file_name(self.foto.name, 'images/')
            if self.foto and not self.imagen_portada_exists():
                super(BannerPrincipal, self).save()
            else:
                self.foto = self.get_upload_path(self.foto.name, 'images/')  # Avoid saving the file again



            # Always save the instance even if the files are not updated
            super(BannerPrincipal, self).save(*args, **kwargs)

    def imagen_portada_exists(self):
        return default_storage.exists(self.get_upload_path(self.foto.name, 'images/'))

    def get_upload_path(self, filename, path):
        """
        Construct the full file path within the media directory
        """
        return os.path.join(path, filename)

    def normalize_file_name(self, filename, path):
        """
        Normalize and possibly clean up file names to match how Django would handle them on upload.
        """
        # You might want to further enhance this normalization
        base, ext = os.path.splitext(filename)
        return slugify(base) + ext.lower()




        # super().save(*args, **kwargs)





class Iconos (ImageManagementMixin):
    class Meta:
        verbose_name_plural = "Iconos"
    ICON_CHOICES = [
        ('S_Efemerides', 'Sección Efemerides'),
        ('S_BannerPpal', 'Sección Banner Principal'),
        ('S_Eventos', 'Sección Eventos'),
        ('S_Revista', 'Sección Revista'),

    ]

    seccion = models.CharField(max_length=50, choices=ICON_CHOICES, blank=False, null=False)
    foto = models.FileField(upload_to='logos/', blank=False, null=False, max_length=500)


    def __str__(self):
        return self.seccion


class Evento (ImageManagementMixin):
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
    foto = models.FileField(upload_to='images/', max_length=500, null=True)

    def get_foto_url(objeto):
        """
        Devuelve la URL completa de la foto de un objeto, asumiendo que el objeto tiene un campo 'foto'.
        """
        if objeto.foto and hasattr(objeto.foto, 'url'):
            return 'https://back.dcubamusica.cult.cu/public/' + objeto.foto.url
        return None



    def __str__(self):
        return str(self.titulo)


class Historia_de_la_Institución (ImageManagementMixin):
    class Meta:
        verbose_name_plural = "Historia de la Institución"
    titulo = RichTextField(config_name = 'small', blank=False, null=False)
    descripcion = RichTextField(blank=False, null=False)
    foto = models.FileField(upload_to='images/', max_length=500,blank=True, null=True)

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
    correo = models.EmailField(max_length=500,blank=False, null=False)

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

class Directores(ImageManagementMixin):
    class Meta:
        verbose_name_plural = "Directores"

    nombre = RichTextField(config_name='small', blank=False, null=False)
    foto = models.FileField(upload_to='images/', default='images/blank.webp', blank=True,null=True)
    cargo = models.CharField(max_length=500, blank=False, null=False)
    télefono = models.CharField(max_length=20, blank=False, null=False)  # Corregido 'télefono' por 'telefono'
    correo = models.EmailField(blank=False, null=False)
    consejo_de_dirección = models.BooleanField(default=False, blank=True,null=True)  # Cambiado 'null=False' por 'default=False'
    empresa = models.OneToOneField("Centros_y_Empresas", on_delete=models.CASCADE, blank=False, null=False)
    es_ceo = models.BooleanField(default=False, verbose_name="¿Es CEO?")  # Campo booleano para CEO
    es_cto = models.BooleanField(default=False, verbose_name="¿Es CTO?")  # Campo booleano para CTO

    def get_foto_url(self):
        return self.foto.url if self.foto else 'https://back.dcubamusica.cult.cu/public/images/blank.webp'

    def __str__(self):
        return str(self.nombre)

class Premio_Nacional_de_Música (ImageManagementMixin):
    class Meta:
        verbose_name_plural = "Premio Nacional de Música"
    titulo = RichTextField(config_name = 'small', blank=False, null=False)
    año = models.IntegerField(blank = False, null=False)
    descripcion = RichTextField(blank=False, null=False)
    bibliografía = RichTextField(config_name = 'small', blank=True, null=True)
    foto = models.FileField(upload_to='images/', max_length=500, blank=True, null=True)


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

class Acontecimiento (ImageManagementMixin):
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
    foto = models.FileField(upload_to='images/', max_length=500, blank=False, null=False)

    def get_foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return 'https://back.dcubamusica.cult.cu/public/' + self.foto.url

    def __str__(self):
        return str(self.titulo)


class Multimedia (ImageManagementMixin):
    class Meta:
        verbose_name_plural = "Multimedias"
    titulo = RichTextField(config_name = 'small', blank=False, null=False)

    descripcion = RichTextField(blank=False, null=False)
    tipo = models.CharField(max_length=500)
    enlace = models.URLField(max_length=200,blank=True, null=True)
    archivo = models.FileField(upload_to='multimedias/', blank=True, null=True)
    foto = models.FileField(upload_to='multimedias/', max_length=500,blank=True, null=True)

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
        return str(self.titulo)

class Efemerides (ImageManagementMixin):
    class Meta:
        verbose_name_plural = "Efemérides"
    titulo = RichTextField(config_name = 'small', blank=False, null=False)
    fecha = models.DateField(blank=False, null=False)
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
    foto = models.FileField(upload_to='images/', max_length=500, blank=True, null=True)

    def get_foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            return 'https://back.dcubamusica.cult.cu/public/' + self.foto.url


    def __str__(self):
        return str(self.titulo)



class Redes (ImageManagementMixin):
    class Meta:
        verbose_name_plural = "Redes"
    titulo = RichTextField(config_name = 'small', blank=False, null=False)
    enlace = models.URLField(max_length=200,blank=True, null=True)
    foto = models.FileField(upload_to='redes/', max_length=500,blank=True, null=True)


    def __str__(self):
        return str(self.titulo)
