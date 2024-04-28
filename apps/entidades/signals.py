
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Efemerides, Acontecimiento, Evento, BannerPrincipal

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
