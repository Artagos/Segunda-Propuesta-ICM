
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.storage import default_storage
from django.utils.text import slugify
import os
from .models import Podcast, Iconos, Revista, Evento, Premio_Nacional_de_Música, Acontecimiento, Historia_de_la_Institución, Centros_y_Empresas, Directores, Multimedia, Efemerides, Redes, BannerPrincipal

@receiver(post_save, sender=Revista)
def prevent_duplicate_files(sender, instance, **kwargs):
    if hasattr(instance, 'imagen_portada') and instance.imagen_portada:
        normalized_path = instance.normalize_file_name(instance.imagen_portada.name, 'images/')
        if default_storage.exists(normalized_path):
            instance.imagen_portada = normalized_path

    if hasattr(instance, 'pdf') and instance.pdf:
        normalized_path = instance.normalize_file_name(instance.pdf.name, 'pdfs/')
        if default_storage.exists(normalized_path):
            instance.pdf = normalized_path


@receiver(post_save, sender=Podcast)
def prevent_duplicate_files1(sender, instance, **kwargs):
    if hasattr(instance, 'foto') and instance.foto:
        normalized_path = instance.normalize_file_name(instance.foto.name, 'images/')
        if default_storage.exists(normalized_path):
            instance.foto = normalized_path

    if hasattr(instance, 'archivo_local') and instance.archivo_local:
        normalized_path = instance.normalize_file_name(instance.archivo_local.name, 'podcast/')
        if default_storage.exists(normalized_path):
            instance.archivo_local = normalized_path





@receiver(post_save, sender=Iconos)
@receiver(post_save, sender=Evento)
@receiver(post_save, sender=Premio_Nacional_de_Música)
@receiver(post_save, sender=Acontecimiento)
@receiver(post_save, sender=Historia_de_la_Institución)
@receiver(post_save, sender=Directores)
@receiver(post_save, sender=Multimedia)
@receiver(post_save, sender=Efemerides)
@receiver(post_save, sender=Redes)
@receiver(post_save, sender=BannerPrincipal)
def prevent_duplicate_files2(sender, instance, **kwargs):
    # Comprobar la imagen de portada
    if instance.foto:
        foto_path = instance.foto.name
        if default_storage.exists(foto_path):
            instance.foto = foto_path



@receiver(post_save, sender=Efemerides)
def update_banner_from_efemerides(sender, instance, **kwargs):
    banners = BannerPrincipal.objects.filter(seleccionar_efemeride=instance)
    for banner in banners:
        banner.titulo = instance.titulo
        banner.descripcion = instance.descripcion
        banner.foto = instance.foto
        banner.color_de_fondo = instance.color_de_fondo
        banner.encabezado = instance.encabezado
        banner.save()

@receiver(post_save, sender=Acontecimiento)
def update_banner_from_acontecimiento(sender, instance, **kwargs):
    banners = BannerPrincipal.objects.filter(seleccionar_acontecimiento=instance)
    for banner in banners:
        banner.titulo = instance.titulo
        banner.descripcion = instance.descripcion
        banner.foto = instance.foto
        banner.color_de_fondo = instance.color_de_fondo
        banner.encabezado = instance.encabezado
        banner.save()

@receiver(post_save, sender=Evento)
def update_banner_from_evento(sender, instance, **kwargs):
    banners = BannerPrincipal.objects.filter(seleccionar_evento=instance)
    for banner in banners:
        banner.titulo = instance.titulo
        banner.descripcion = instance.descripcion
        banner.foto = instance.foto
        banner.color_de_fondo = instance.color_de_fondo
        banner.encabezado = instance.encabezado
        banner.save()


def normalize_file_name(self, filename, path):
        """
        Normalize and possibly clean up file names to match how Django would handle them on upload.
        """
        # You might want to further enhance this normalization
        base, ext = os.path.splitext(filename)
        return slugify(base) + ext.lower()