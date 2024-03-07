import json
from django.shortcuts import render
from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from calendar import monthrange
from django.http import JsonResponse
from .models import Efemerides, Acontecimiento, Evento, Centros_y_Empresas, Directores, Historia_de_la_Institución, Multimedia, Premio_Nacional_de_Música, Iconos
from .models import BannerPrincipal, Seccion_Efemerides
from django.core.exceptions import ObjectDoesNotExist


def get_banner_principal(request):
    contenedores = BannerPrincipal.objects.all().order_by('numero_unico').values()
    return JsonResponse(list(contenedores), safe=False)

def get_seccion_efemerides(request):
    contenedores = Seccion_Efemerides.objects.all().order_by('numero_unico').values()
    return JsonResponse(list(contenedores), safe=False)




def get_iconos(request):

    iconos_max_id = Iconos.objects.values('seccion').annotate(max_id=Max('id'))


    iconos_ids = [icono['max_id'] for icono in iconos_max_id]

    iconos_seleccionados = Iconos.objects.filter(id__in=iconos_ids)


    iconos_data = [
        {
            'seccion': icono.get_seccion_display(),
            'foto': request.build_absolute_uri(icono.foto.url) if icono.foto else None
        }
        for icono in iconos_seleccionados
    ]

    return JsonResponse({'iconos': iconos_data})



def get_all_efem(request):
    efemerides = Efemerides.objects.all().order_by().values()
    return JsonResponse(list(efemerides), safe=False)

def get_efem_premio(request):
    efemerides = Efemerides.objects.get(premio_nacional_de_la_música is not None).values()
    return JsonResponse(list(efemerides), safe=False)

def get_efem_a_mostrar(request):
    efemerides = Efemerides.objects.get(mostrar_en_banner_principal = true).values()
    return JsonResponse(list(efemerides), safe=False)

def get_acontecimiento_relevante(request):
    acontecimiento = Acontecimiento.objects.get(relevante = true).values()
    return JsonResponse(list(acontecimiento), safe=False)


def get_acontecimiento_a_mostrar(request):
    acontecimiento = Acontecimiento.objects.get(mostrar_en_banner_principal = true).values()
    return JsonResponse(list(acontecimiento), safe=False)

def get_evento_a_mostrar(request):
    evento = Evento.objects.get(mostrar_en_banner_principal = true).values()
    return JsonResponse(list(evento), safe=False)

def get_historia(request):
    historia = Historia.objects.all().values()
    return JsonResponse(list(historia), safe=False)

def get_centros_y_directores(request):
    centros_y_directores = Directores.objects.select_related('empresa').all().values()
    return JsonResponse(list(centros_y_directores), safe=False)

def get_premios(request):
    premios = Premio_Nacional_de_Música.objects.order_by('fecha').values()
    return JsonResponse(list(premios), safe=False)

def get_acontecimientos_semana(request):
    fecha = datetime.now()
    fecha_inicio = fecha - timedelta(days = fecha.weekday())
    fecha_fin = fecha_inicio + timedelta(days = 6)
    acontecimientos_semana = Acontecimiento.objects.filter(fecha__range = [fecha_inicio, fecha_fin]).values()
    return JsonResponse(list(acontecimientos_semana), safe=False)

def get_eventos_semana(request):
    fecha = datetime.now()
    fecha_inicio = fecha - timedelta(days = fecha.weekday())
    fecha_fin = fecha_inicio + timedelta(days = 6)
    eventos_semana = Evento.objects.filter(fecha__range = [fecha_inicio, fecha_fin]).values()
    return JsonResponse(list(eventos_semana), safe=False)

def get_acontecimientos_mes(request):
    fecha = datetime.now()
    fecha_inicio = fecha.replace(day = 1)
    fecha_fin = fecha_inici0.replace(day= monthrange(fecha.year, fecha.month)[1])
    acontecimientos_mes = Acontecimiento.objects.filter(fecha__range = [fecha_inicio, fecha_fin]).values()
    return JsonResponse(list(acontecimientos_mes), safe=False)

def get_eventos_mes(request):
    fecha = datetime.now()
    fecha_inicio = fecha.replace(day = 1)
    fecha_fin = fecha_inici0.replace(day= monthrange(fecha.year, fecha.month)[1])
    eventos_mes = Eventos.objects.filter(fecha__range = [fecha_inicio, fecha_fin]).values()
    return JsonResponse(list(eventos_mes), safe=False)

def get_centros_contactos(request):
    centros = Centros_y_Empresas.objects.all().values()
    data = [
        {
            'nombre': centro.nombre,
            'telefono': centro.teléfono,
            'email': centro.correo,
        }
        for centro in centros
    ]
    return JsonResponse(data, safe=False)

def get_directores_nombres(request):
    directores = Directores.objects.all().values()
    data = [
        {
            'nombre': director.nombre,

        }
        for director in directores
    ]
    return JsonResponse(data, safe=False)