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
from django.utils import translation


import os



class ImageManagementMixinBanner(models.Model):
    """
    Mixin para manejar la verificación y reutilización de archivos de imágenes existentes en entidades relacionadas.
    """
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        current_language = get_language()

        # Asigna atributos basados en la selección y el idioma
        if self.seleccionar_efemeride:
            selected = self.seleccionar_efemeride
        elif self.seleccionar_acontecimiento:
            selected = self.seleccionar_acontecimiento
        elif self.seleccionar_evento:
            selected = self.seleccionar_evento
        else:
            selected = None

        if selected:
            self.titulo = getattr(selected, f'titulo_{current_language}', "")
            self.descripcion = getattr(selected, f'descripcion_{current_language}', "")
            self.encabezado = getattr(selected, f'encabezado_{current_language}', "")
            self.foto = selected.foto
            self.color_de_fondo = selected.color_de_fondo

        if hasattr(self, 'foto') and self.foto:
            normalized_name = self.normalize_file_name(self.foto.name)
            print(normalized_name)
            file_path = self.get_upload_path(normalized_name)

            if default_storage.exists(file_path):
                # Si el archivo ya existe, se reutiliza la misma ruta sin guardar el archivo de nuevo
                # Solo actualiza el nombre para reflejar la ubicación correcta
                self.foto.name = file_path
            else:
                # Si el archivo no existe, procede con el guardado normal
                # Asegúrate de actualizar el nombre del archivo al nombre normalizado completo
                self.foto.name = normalized_name
                super(ImageManagementMixinBanner, self).save(*args, **kwargs)  # Guarda el modelo con el nuevo archivo
                return  # Salir para evitar guardado duplicado
        else:
            # Si no hay foto o el atributo 'foto' no existe, guarda normalmente
            super(ImageManagementMixinBanner, self).save(*args, **kwargs)# Guarda el modelo normalmente si no se cumple la condición anterior

    def normalize_file_name(self, filename):
        """
        Normaliza y limpia los nombres de los archivos para coincidir con cómo Django los manejaría en la carga.
        """
        # Extrae el nombre del archivo de la ruta completa
        base_name = os.path.basename(filename)
        base, ext = os.path.splitext(base_name)
        return slugify(base) + ext.lower()

    def get_upload_path(self, filename):
        """
        Construye la ruta de carga basada en el directorio 'images/'
        """
        return os.path.join('images/', filename)


class ImageManagementMixin(models.Model):
    """
    Mixin para manejar la verificación y reutilización de archivos de imágenes existentes.
    """
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Este método asume que el campo de la imagen se llama 'foto'
        if hasattr(self, 'foto') and self.foto:
            # Normaliza el nombre del archivo sin alterar la ruta de guardado
            normalized_name = self.normalize_file_name(self.foto.name)
            # Construye la ruta completa donde se guardaría la imagen
            file_path = self.get_upload_path(normalized_name)

            if default_storage.exists(file_path):
                # Si el archivo ya existe, reutiliza la misma ruta
                self.foto = 'images/' + self.foto.name
            else:
                # Si el archivo no existe, procede con el guardado normal
                self.foto = 'images/' + self.foto.name
                super(ImageManagementMixin, self).save(*args, **kwargs)
                return  # Sal del método después de guardar para evitar llamadas duplicadas a save()

        # Si no hay foto o el atributo 'foto' no existe, o el archivo ya existe y no necesita ser guardado de nuevo
        super(ImageManagementMixin, self).save(*args, **kwargs)

    def normalize_file_name(self, filename):
        """
        Normaliza y limpia los nombres de los archivos para coincidir con cómo Django los manejaría en la carga.
        """
        # Extrae el nombre del archivo de la ruta completa
        base_name = os.path.basename(filename)
        base, ext = os.path.splitext(base_name)
        return slugify(base) + ext.lower()

    def get_upload_path(self, filename):
        """
        Construye la ruta de carga basada en el directorio 'images/'
        """
        return os.path.join('images/', filename)




class ImageManagementMixinRevista(models.Model):
    """
    Mixin para manejar la verificación y reutilización de archivos de imágenes existentes.
    """
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Este método asume que el campo de la imagen se llama 'foto'
        if hasattr(self, 'imagen_portada') and self.imagen_portada:
            # Normaliza el nombre del archivo sin alterar la ruta de guardado
            normalized_name = self.normalize_file_name(self.imagen_portada.name)
            # Construye la ruta completa donde se guardaría la imagen
            file_path = self.get_upload_path(normalized_name)

            if default_storage.exists(file_path):
                # Si el archivo ya existe, reutiliza la misma ruta
                self.imagen_portada = 'images/' + self.imagen_portada.name
            else:
                # Si el archivo no existe, procede con el guardado normal
                self.imagen_portada = 'images/' + self.imagen_portada.name
                super(ImageManagementMixinRevista, self).save(*args, **kwargs)
                return  # Sal del método después de guardar para evitar llamadas duplicadas a save()

        if hasattr(self, 'pdf') and self.pdf:
            normalized_name = self.normalize_file_name(self.pdf.name)
            # Construye la ruta completa donde se guardaría la imagen
            file_path = self.get_upload_path2(normalized_name)

            if default_storage.exists(file_path):
                # Si el archivo ya existe, reutiliza la misma ruta
                self.pdf = 'pdfs/' + self.pdf.name
            else:
                # Si el archivo no existe, procede con el guardado normal
                self.pdf = 'pdfs/' + self.pdf.name
                super(ImageManagementMixinRevista, self).save(*args, **kwargs)
                return

        # Si no hay foto o el atributo 'foto' no existe, o el archivo ya existe y no necesita ser guardado de nuevo
        super(ImageManagementMixinRevista, self).save(*args, **kwargs)

    def normalize_file_name(self, filename):
        """
        Normaliza y limpia los nombres de los archivos para coincidir con cómo Django los manejaría en la carga.
        """
        # Extrae el nombre del archivo de la ruta completa
        base_name = os.path.basename(filename)
        base, ext = os.path.splitext(base_name)
        return slugify(base) + ext.lower()

    def get_upload_path(self, filename):
        """
        Construye la ruta de carga basada en el directorio 'images/'
        """
        return os.path.join('images/', filename)

    def get_upload_path2(self, filename):
        """
        Construye la ruta de carga basada en el directorio 'images/'
        """
        return os.path.join('pdfs/', filename)

# class ImageManagementMixin(models.Model):
#     """
#     Mixin para manejar la verificación y reutilización de archivos de imágenes existentes.
#     """
#     class Meta:
#         abstract = True

#     def save(self, *args, **kwargs):
#         # Este método asume que el campo de la imagen se llama 'foto'
#         if hasattr(self, 'foto') and self.foto:
#             # Normaliza el nombre del archivo sin alterar la ruta de guardado
#             normalized_name = self.normalize_file_name(self.foto.name)
#             # Construye la ruta completa donde se guardaría la imagen
#             file_path = self.get_upload_path(normalized_name)

#             if default_storage.exists(file_path):
#                 # Si el archivo ya existe, reutiliza la misma ruta
#                 self.foto.name = normalized_name
#             else:
#                 # Si el archivo no existe, procede con el guardado normal
#                 self.foto.name = normalized_name
#                 super(ImageManagementMixin, self).save(*args, **kwargs)
#         else:
#             # Si no hay foto o el atributo 'foto' no existe, guarda normalmente
#             super(ImageManagementMixin, self).save(*args, **kwargs)

#     def normalize_file_name(self, filename):
#         """
#         Normaliza y limpia los nombres de los archivos para coincidir con cómo Django los manejaría en la carga.
#         """
#         base, ext = os.path.splitext(filename)
#         return slugify(base) + ext.lower()

#     def get_upload_path(self, filename):
#         """
#         Construye la ruta de carga basada en el directorio 'images/'
#         """
#         return os.path.join('images/', filename)


class Revista(ImageManagementMixinRevista):
    titulo_es = RichTextField(config_name='small', blank=False, null=False)
    descripcion_es = RichTextField(blank=False, null=False)
    titulo_en = RichTextField(default= 'a',config_name='small', blank=False, null=False)
    descripcion_en = RichTextField(default= 'a', blank=False, null=False)
    fecha = models.DateField(blank=False, null=False)
    pdf = models.FileField(upload_to='pdfs/', blank=False, null=False,max_length=500)
    imagen_portada = models.ImageField(upload_to='images/',blank=False, null=False,max_length=500)


    def __str__(self):
        # Obtener el idioma actualmente activo
        current_language = translation.get_language()

        # Devolver el título correspondiente al idioma activo
        if current_language == 'es':
            return str(self.titulo_es)
        elif current_language == 'en':
            return str(self.titulo_en)

    # # def save(self, *args, **kwargs):
    # #     self.imagen_portada = 'images/' + self.imagen_portada.name
    # #     if self.imagen_portada and not self.imagen_portada_exists():
    # #         super(Revista, self).save()
    # #     else:
    # #         self.imagen_portada = 'images/' + self.imagen_portada.name # Avoid saving the file again

    # #     normalized_name = self.normalize_file_name(self.pdf.name)
    # #         # Construye la ruta completa donde se guardaría la imagen
    # #     file_path = self.get_upload_path2(normalized_name)

    # #     if default_storage.exists(file_path):
    # #         # Si el archivo ya existe, reutiliza la misma ruta
    # #         self.pdf = 'pdfs/' + self.pdf.name
    # #     else:
    # #         # Si el archivo no existe, procede con el guardado normal
    # #         self.pdf = 'pdfs/' + self.pdf.name
    # #         super(Revista, self).save(*args, **kwargs)
    # #         return

    # #     # self.pdf = 'pdfs/' + self.pdf.name
    # #     # if self.pdf and not self.pdf_exists():
    # #     #     super(Revista, self).save()
    # #     # else:
    # #     #     self.pdf = 'pdfs/' + self.pdf.name # Avoid saving the file again

    # #     # Always save the instance even if the files are not updated
    # #     super(Revista, self).save(*args, **kwargs)

    # def get_upload_path2(self, filename):
    #     """
    #     Construye la ruta de carga basada en el directorio 'images/'
    #     """
    #     return os.path.join('images/', filename)

    # def normalize_file_name(self, filename):
    #     """
    #     Normaliza y limpia los nombres de los archivos para coincidir con cómo Django los manejaría en la carga.
    #     """
    #     # Extrae el nombre del archivo de la ruta completa
    #     base_name = os.path.basename(filename)
    #     base, ext = os.path.splitext(base_name)
    #     return slugify(base) + ext.lower()

    # def imagen_portada_exists(self):
    #     return default_storage.exists(self.get_upload_path(self.imagen_portada.name, 'images/'))

    # def pdf_exists(self):
    #     return default_storage.exists(self.get_upload_path(self.pdf.name, 'pdfs/'))

    # def get_upload_path(self, filename, path):
    #     """
    #     Construct the full file path within the media directory
    #     """
    #     return os.path.join(path, filename)

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
    titulo_es = RichTextField(config_name = 'small',blank=False, null=False)
    descripcion_es = RichTextField(blank=False, null=False)
    titulo_en = RichTextField(config_name='small', blank=False, null=False)
    descripcion_en = RichTextField(blank=False, null=False)
    link_podcast = models.URLField(blank=False, null=False)  # Puede contener tanto URLs locales como externas
    archivo_local = models.FileField(upload_to='podcast/', blank=False, null=False,max_length=500)
    foto = models.ImageField(upload_to='images/',blank=False, null=False,max_length=500)

    def save(self, *args, **kwargs):
        # Check and set for image
        if self.foto:
            self.foto.name = self.normalize_file_name(self.foto.name)
            if not self.file_exists(self.foto.name, 'images/'):
                super(Podcast, self).save(*args, **kwargs)
            else:
                self.foto = self.get_upload_path(self.foto.name, 'images/')

        # Check and set for mp3
        if self.archivo_local:
            self.archivo_local.name = self.normalize_file_name(self.archivo_local.name)
            if not self.file_exists(self.archivo_local.name, 'podcast/'):
                # super(Podcast, self).save(*args, **kwargs)
                pass
            else:
                self.archivo_local = self.get_upload_path(self.archivo_local.name, 'podcast/')

        # Always save the instance even if the files are not updated
        super(Podcast, self).save(*args, **kwargs)

    def file_exists(self, filename, path):
        full_path = self.get_upload_path(filename, path)
        return default_storage.exists(full_path)

    def get_upload_path(self, filename, path):
        return os.path.join(path, filename)

    def normalize_file_name(self, filename):
        """
        Normaliza y limpia los nombres de los archivos para coincidir con cómo Django los manejaría en la carga.
        """
        # Extrae el nombre del archivo de la ruta completa
        base_name = os.path.basename(filename)
        base, ext = os.path.splitext(base_name)
        return slugify(base) + ext.lower()



    def __str__(self):
        # Obtener el idioma actualmente activo
        current_language = translation.get_language()

        # Devolver el título correspondiente al idioma activo
        if current_language == 'es':
            return str(self.titulo_es)
        elif current_language == 'en':
            return str(self.titulo_en)


# class ContenedorConFondo (models.Model):
#     titulo_es = models.CharField(max_length=50)
#     descripcion_es = models.CharField(max_length=500)
#     foto = models.FileField(upload_to='images/', max_length=500)

# class ContenedorConFondoSolotitulo_es (models.Model):
#     titulo_es = models.CharField(max_length=50)
#     foto = models.FileField(upload_to='images/', max_length=500)

# class ContenedorICM (models.Model):
#     titulo_es = models.CharField(max_length=50)
#     encabezado_es = models.CharField(max_length=50)
#     descripcion_es = models.CharField(max_length=500)
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
        ('ContenedorConFondoSolotitulo_es', 'Tipo 2'),
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
    titulo_es = RichTextField(config_name = 'small', blank=False, null=False)
    titulo_en = RichTextField(config_name='small', blank=False, null=False)
    descripcion_en = RichTextField(blank=False, null=False)
    encabezado_es = RichTextField(config_name = 'small', blank=False, null=False)
    encabezado_en = RichTextField(config_name = 'small', blank=False, null=False)
    descripcion_es = RichTextField(blank=False, null=False)
    foto = models.FileField(upload_to='images/', max_length=500, null=True)








    color_de_fondo = models.CharField(max_length=7, choices=TEXT_COLOR_CHOICES, null=True,default='#ffffff')
    numero_unico = models.PositiveIntegerField(unique=True, blank=False, null=False)



    def __str__(self):
        current_language = translation.get_language()

        # Devolver el título correspondiente al idioma activo
        if current_language == 'es':
            if self.seleccionar_efemeride and self.seleccionar_efemeride.titulo_es:
                return str(self.seleccionar_efemeride.titulo_es)
            elif self.seleccionar_acontecimiento and self.seleccionar_acontecimiento.titulo_es:
                return str(self.seleccionar_acontecimiento.titulo_es)
            elif self.seleccionar_evento and self.seleccionar_evento.titulo_es:
                return str(self.seleccionar_evento.titulo_es)
            else:
                return str(self.titulo_es)

        elif current_language == 'en':
            if self.seleccionar_efemeride and self.seleccionar_efemeride.titulo_en:
                return str(self.seleccionar_efemeride.titulo_en)
            elif self.seleccionar_acontecimiento and self.seleccionar_acontecimiento.titulo_en:
                return str(self.seleccionar_acontecimiento.titulo_en)
            elif self.seleccionar_evento and self.seleccionar_evento.titulo_en:
                return str(self.seleccionar_evento.titulo_en)
            else:
                return str(self.titulo_en)

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

            super().save(*args, **kwargs)

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

            super().save(*args, **kwargs)

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

            super().save(*args, **kwargs)

        else:
            if hasattr(self, 'foto') and self.foto:
            # Normaliza el nombre del archivo sin alterar la ruta de guardado
                normalized_name = self.normalize_file_name(self.foto.name)
                # Construye la ruta completa donde se guardaría la imagen
                file_path = self.get_upload_path(normalized_name)

                if default_storage.exists(file_path):
                    # Si el archivo ya existe, reutiliza la misma ruta
                    self.foto = 'images/' + self.foto.name
                else:
                    # Si el archivo no existe, procede con el guardado normal
                    self.foto = 'images/' + self.foto.name
                    super(BannerPrincipal, self).save(*args, **kwargs)
                    return  # Sal del método después de guardar para evitar llamadas duplicadas a save()

            # Si no hay foto o el atributo 'foto' no existe, o el archivo ya existe y no necesita ser guardado de nuevo
                super(BannerPrincipal, self).save(*args, **kwargs)


    def normalize_file_name(self, filename):
        """
        Normaliza y limpia los nombres de los archivos para coincidir con cómo Django los manejaría en la carga.
        """
        base, ext = os.path.splitext(filename)
        return slugify(base) + ext.lower()

    def get_upload_path(self, filename):
        """
        Construye la ruta de carga basada en el directorio 'images/'
        """
        # Asegúrate de que filename no comienza con una barra
        if filename.startswith('images'):
            filename = filename[6:]
        return os.path.join('images/', filename)



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

    titulo_es = RichTextField(config_name = 'small', blank=False, null=False)
    titulo_en = RichTextField(config_name='small', blank=False, null=False)
    descripcion_en = RichTextField(blank=False, null=False)
    fecha = models.DateField()
    encabezado_es = RichTextField(blank=False, null=False)
    encabezado_en = RichTextField(blank=False, null=False)
    descripcion_es = RichTextField(blank=False, null=False)
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
        # Obtener el idioma actualmente activo
        current_language = translation.get_language()

        # Devolver el título correspondiente al idioma activo
        if current_language == 'es':
            return str(self.titulo_es)
        elif current_language == 'en':
            return str(self.titulo_en)


class Historia_de_la_Institución (ImageManagementMixin):
    class Meta:
        verbose_name_plural = "Historia de la Institución"
    titulo_es = RichTextField(config_name = 'small', blank=False, null=False)
    descripcion_es = RichTextField(blank=False, null=False)
    titulo_en = RichTextField(config_name='small', blank=False, null=False)
    descripcion_en = RichTextField(blank=False, null=False)
    foto = models.FileField(upload_to='images/', max_length=500,blank=False, null=False)

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
        # Obtener el idioma actualmente activo
        current_language = translation.get_language()

        # Devolver el título correspondiente al idioma activo
        if current_language == 'es':
            return str(self.titulo_es)
        elif current_language == 'en':
            return str(self.titulo_en)

class Centros_y_Empresas (models.Model):
    class Meta:
        verbose_name_plural = "Centros y Empresas"
    nombre_es = RichTextField(config_name = 'small', blank=False, null=False)
    nombre_en = RichTextField(config_name = 'small', blank=False, null=False)
    dirección_es = models.CharField(max_length=500,blank=False, null=False)
    dirección_en = models.CharField(max_length=500,blank=False, null=False)
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
        # Obtener el idioma actualmente activo
        current_language = translation.get_language()

        # Devolver el título correspondiente al idioma activo
        if current_language == 'es':
            return str(self.nombre_es)
        elif current_language == 'en':
            return str(self.nombre_en)

class Directores(ImageManagementMixin):
    class Meta:
        verbose_name_plural = "Directores"

    nombre_es = RichTextField(config_name='small', blank=False, null=False)
    foto = models.FileField(upload_to='images/', default='blank.webp', blank=True,null=True)
    cargo_es = models.CharField(max_length=500, blank=False, null=False)
    nombre_en = RichTextField(config_name='small', blank=False, null=False)

    cargo_en = models.CharField(max_length=500, blank=False, null=False)
    télefono = models.CharField(max_length=20, blank=False, null=False)  # Corregido 'télefono' por 'telefono'
    correo = models.EmailField(blank=False, null=False)
    consejo_de_dirección = models.BooleanField(default=False, blank=True,null=True)  # Cambiado 'null=False' por 'default=False'
    empresa = models.ForeignKey("Centros_y_Empresas", on_delete=models.CASCADE, blank=False, null=False)
    es_ceo = models.BooleanField(default=False, verbose_name="¿Es CEO?")  # Campo booleano para CEO
    es_cto = models.BooleanField(default=False, verbose_name="¿Es CTO?")  # Campo booleano para CTO

    def get_foto_url(self):
        return self.foto.url if self.foto else 'https://back.dcubamusica.cult.cu/public/images/blank.webp'

    def __str__(self):
        # Obtener el idioma actualmente activo
        current_language = translation.get_language()

        # Devolver el título correspondiente al idioma activo
        if current_language == 'es':
            return str(self.nombre_es)
        elif current_language == 'en':
            return str(self.nombre_en)

class Premio_Nacional_de_Música (ImageManagementMixin):
    class Meta:
        verbose_name_plural = "Premio Nacional de Música"
    titulo_es = RichTextField(config_name = 'small', blank=False, null=False)
    titulo_en = RichTextField(config_name='small', blank=False, null=False)
    descripcion_en = RichTextField(blank=False, null=False)
    año = models.IntegerField(blank = False, null=False)
    descripcion_es = RichTextField(blank=False, null=False)
    bibliografía_es = RichTextField(config_name = 'small', blank=False, null=False)
    bibliografía_en = RichTextField(config_name = 'small', blank=False, null=False)

    foto = models.FileField(upload_to='images/', max_length=500, blank=False, null=False)


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
        # Obtener el idioma actualmente activo
        current_language = translation.get_language()

        # Devolver el título correspondiente al idioma activo
        if current_language == 'es':
            return str(self.titulo_es)
        elif current_language == 'en':
            return str(self.titulo_en)

class Acontecimiento (ImageManagementMixin):
    class Meta:
        verbose_name_plural = "Acontecimientos"

    titulo_es = RichTextField(config_name = 'small', blank=False, null=False)
    titulo_en = RichTextField(config_name='small', blank=False, null=False)
    descripcion_en = RichTextField(blank=False, null=False)
    fecha = models.DateField(blank=False, null=False)
    encabezado_es = RichTextField(blank=False, null=False)
    encabezado_en = RichTextField(blank=False, null=False)
    descripcion_es = RichTextField(blank=False, null=False)
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




    def __str__(self):
        # Obtener el idioma actualmente activo
        current_language = translation.get_language()

        # Devolver el título correspondiente al idioma activo
        if current_language == 'es':
            return str(self.titulo_es)
        elif current_language == 'en':
            return str(self.titulo_en)


class Multimedia (ImageManagementMixin):
    class Meta:
        verbose_name_plural = "Multimedias"
    titulo_es = RichTextField(config_name = 'small', blank=False, null=False)

    descripcion_es = RichTextField(blank=False, null=False)
    titulo_en = RichTextField(config_name='small', blank=False, null=False)
    descripcion_en = RichTextField(blank=False, null=False)

    tipo = models.CharField(max_length=500)
    enlace = models.URLField(max_length=200,blank=False, null=False)
    archivo = models.FileField(upload_to='multimedias/', blank=False, null=False)
    foto = models.FileField(upload_to='multimedias/', max_length=500,blank=False, null=False)




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
        # Obtener el idioma actualmente activo
        current_language = translation.get_language()

        # Devolver el título correspondiente al idioma activo
        if current_language == 'es':
            return str(self.titulo_es)
        elif current_language == 'en':
            return str(self.titulo_en)

class Efemerides (ImageManagementMixin):
    class Meta:
        verbose_name_plural = "Efemérides"
    titulo_es = RichTextField(config_name = 'small', blank=False, null=False)
    titulo_en = RichTextField(config_name='small', blank=False, null=False)
    descripcion_en = RichTextField(blank=False, null=False)

    encabezado_en = RichTextField(blank=False, null=False)
    fecha = models.DateField(blank=False, null=False)
    encabezado_es = RichTextField(blank=False, null=False)
    descripcion_es = RichTextField(blank=False, null=False)

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





    def __str__(self):
        # Obtener el idioma actualmente activo
        current_language = translation.get_language()

        # Devolver el título correspondiente al idioma activo
        if current_language == 'es':
            return str(self.titulo_es)
        elif current_language == 'en':
            return str(self.titulo_en)



class Redes (ImageManagementMixin):
    class Meta:
        verbose_name_plural = "Redes"
    titulo_es = RichTextField(config_name = 'small', blank=False, null=False)
    titulo_en = RichTextField(config_name='small', blank=False, null=False)
    enlace = models.URLField(max_length=200,blank=False, null=False)
    foto = models.FileField(upload_to='redes/', max_length=500,blank=False, null=False)



    def __str__(self):
        # Obtener el idioma actualmente activo
        current_language = translation.get_language()

        # Devolver el título correspondiente al idioma activo
        if current_language == 'es':
            return str(self.titulo_es)
        elif current_language == 'en':
            return str(self.titulo_en)
