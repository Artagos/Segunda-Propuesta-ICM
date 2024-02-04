from django.shortcuts import render
from datetime import datetime, timedelta
from calendar import monthrange
from django.http import JsonResponse
from .models import Efemerides, Acontecimiento, Evento, Centros_y_Empresas, Directores, Historia_de_la_Institución, Multimedia, Premio_Nacional_de_Música




# Create your views here.
def get_all_efem(request):
    efemerides = Efemerides.objects.all().values()
    return JsonResponse(list(efemerides), safe= false)

def get_efem_premio(request):
    efemerides = Efemerides.objects.get(premio_nacional_de_la_música is not None).values()
    return JsonResponse(list(efemerides), safe= false)
   
def get_efem_a_mostrar(request):
    efemerides = Efemerides.objects.get(mostrar_en_banner_principal = true).values()
    return JsonResponse(list(efemerides), safe= false)

def get_acontecimiento_relevante(request):
    acontecimiento = Acontecimiento.objects.get(relevante = true).values()
    return JsonResponse(list(acontecimiento), safe= false)


def get_acontecimiento_a_mostrar(request):
    acontecimiento = Acontecimiento.objects.get(mostrar_en_banner_principal = true).values()
    return JsonResponse(list(acontecimiento), safe= false)

def get_evento_a_mostrar(request):
    evento = Evento.objects.get(mostrar_en_banner_principal = true).values()
    return JsonResponse(list(evento), safe= false)

def get_historia(request):
    historia = Historia.objects.all().values()
    return JsonResponse(list(historia), safe= false)

def get_centros_y_directores(request):
    centros_y_directores = Directores.objects.select_related('empresa').all().values()
    return JsonResponse(list(centros_y_directores), safe= false)

def get_premios(request):
    premios = Premio_Nacional_de_Música.objects.order_by('fecha').values()
    return JsonResponse(list(premios), safe= false)
    
def get_acontecimientos_semana(request):
    fecha = datetime.now()
    fecha_inicio = fecha - timedelta(days = fecha.weekday())
    fecha_fin = fecha_inicio + timedelta(days = 6)
    acontecimientos_semana = Acontecimiento.objects.filter(fecha__range = [fecha_inicio, fecha_fin]).values()
    return JsonResponse(list(acontecimientos_semana), safe= false)

def get_eventos_semana(request):
    fecha = datetime.now()
    fecha_inicio = fecha - timedelta(days = fecha.weekday())
    fecha_fin = fecha_inicio + timedelta(days = 6)
    eventos_semana = Evento.objects.filter(fecha__range = [fecha_inicio, fecha_fin]).values()
    return JsonResponse(list(eventos_semana), safe= false)

def get_acontecimientos_mes(request):
    fecha = datetime.now()
    fecha_inicio = fecha.replace(day = 1)
    fecha_fin = fecha_inici0.replace(day= monthrange(fecha.year, fecha.month)[1])
    acontecimientos_mes = Acontecimiento.objects.filter(fecha__range = [fecha_inicio, fecha_fin]).values()
    return JsonResponse(list(acontecimientos_mes), safe= false)

def get_eventos_mes(request):
    fecha = datetime.now()
    fecha_inicio = fecha.replace(day = 1)
    fecha_fin = fecha_inici0.replace(day= monthrange(fecha.year, fecha.month)[1])
    eventos_mes = Eventos.objects.filter(fecha__range = [fecha_inicio, fecha_fin]).values()
    return JsonResponse(list(eventos_mes), safe= false)

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
    return JsonResponse(data, safe= false)

def get_directores_nombres(request):
    directores = Directores.objects.all().values()
    data = [
        {
            'nombre': director.nombre,
           
        }
        for director in directores
    ]
    return JsonResponse(data, safe= false)