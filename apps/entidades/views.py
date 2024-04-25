import json
from django.shortcuts import render
from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from calendar import monthrange
from django.http import JsonResponse
from .models import Efemerides, Acontecimiento, Evento, Centros_y_Empresas, Directores, Historia_de_la_Institución, Multimedia, Premio_Nacional_de_Música, Iconos, Revista, BannerPrincipal, Podcast
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.db.models.functions import ExtractMonth, ExtractDay, ExtractYear

def lista_revistas(request):
    revistas = Revista.objects.all()
    contenedores_list = []

    for contenedor in revistas:
        contenedores_list.append({
            'id': contenedor.id,
            'titulo': contenedor.titulo,
            'descripcion': contenedor.descripcion,
            'foto': contenedor.get_foto_url(),
            'pdf':contenedor.get_pdf_url(),
        })

    return JsonResponse(contenedores_list, safe=False)

def detalle_revista(request, id):
    revista = get_object_or_404(Revista, pk=id)
    data = {
        'titulo': revista.titulo,
        'descripcion': revista.descripcion,
        'pdf_url': revista.pdf.url,
        'imagen_portada_url': revista.imagen_portada.url,
    }
    return JsonResponse(data)

def lista_podcasts(request):
    podcasts = Podcast.objects.all()
    podcasts_data = []
    for podcast in podcasts:
        podcast_data = {
            'id': podcast.id,
            'titulo': podcast.titulo,
            'descripcion': podcast.descripcion,
            'link_podcast': podcast.link_podcast,
            'foto': podcast.get_foto_url(),
        }
        podcasts_data.append(podcast_data)
    return JsonResponse(podcasts_data, safe=False)

def get_banner_principal(request):
    contenedores = BannerPrincipal.objects.all().order_by('numero_unico')
    contenedores_list = []

    for contenedor in contenedores:
        contenedor_dict = {
            'id': contenedor.id,
            'tipo_contenedor': contenedor.tipo_contenedor,
            'seleccionar_efemeride': contenedor.seleccionar_efemeride,
            'seleccionar_acontecimiento': contenedor.seleccionar_acontecimiento,
            'seleccionar_evento': contenedor.seleccionar_evento,
            'titulo': contenedor.titulo,
            'descripcion': contenedor.descripcion,
            'foto': contenedor.get_foto_url(),
            'color_de_fondo': contenedor.color_de_fondo,
            'numero_unico': contenedor.numero_unico,
            'encabezado': contenedor.encabezado,
        }

        if contenedor.seleccionar_efemeride is not None:
            efemeride = Efemerides.objects.get(id=contenedor.seleccionar_efemeride)
            contenedor_dict['titulo'] = efemeride.titulo
            contenedor_dict['descripcion'] = efemeride.descripcion
            contenedor_dict['foto'] = efemeride.get_foto_url()
            contenedor_dict['color_de_fondo'] = efemeride.color_de_fondo
            contenedor_dict['encabezado'] = efemeride.encabezado

        elif contenedor.seleccionar_acontecimiento is not None:
            acontecimiento = Acontecimiento.objects.get(id=contenedor.seleccionar_acontecimiento)
            contenedor_dict['titulo'] = acontecimiento.titulo
            contenedor_dict['descripcion'] = acontecimiento.descripcion
            contenedor_dict['foto'] = acontecimiento.get_foto_url()
            contenedor_dict['color_de_fondo'] = acontecimiento.color_de_fondo
            contenedor_dict['encabezado'] = acontecimiento.encabezado
            contenedor_dict['enlace'] = evento.enlace

        elif contenedor.seleccionar_evento is not None:
            evento = Evento.objects.get(id=contenedor.seleccionar_evento)
            contenedor_dict['titulo'] = evento.titulo
            contenedor_dict['descripcion'] = evento.descripcion
            contenedor_dict['foto'] = evento.get_foto_url()
            contenedor_dict['color_de_fondo'] = evento.color_de_fondo
            contenedor_dict['encabezado'] = evento.encabezado
            contenedor_dict['enlace'] = evento.enlace
            contenedor_dict['hora'] = evento.hora

        contenedores_list.append(contenedor_dict)


    return JsonResponse(contenedores_list, safe=False)

def get_iconos(request):

    iconos_max_id = Iconos.objects.values('seccion').annotate(max_id=Max('id'))


    iconos_ids = [icono['max_id'] for icono in iconos_max_id]

    iconos_seleccionados = Iconos.objects.filter(id__in=iconos_ids)


    iconos_data = [
        {
            'seccion': icono.get_seccion_display(),
            'foto': icono.get_foto_url(),
        }
        for icono in iconos_seleccionados
    ]

    return JsonResponse({'iconos': iconos_data})



def get_all_efem(request):
    contenedores = Efemerides.objects.all().order_by().values()
    contenedores_list = []

    for contenedor in contenedores:
        contenedores_list.append({
            'id': contenedor.id,
            'titulo': contenedor.titulo,
            'fecha': contenedor.fecha,
            'descripcion': contenedor.descripcion,
            'foto': contenedor.get_foto_url(),
            'color_de_fondo':contenedor.color_de_fondo,
            'encabezado':contenedor.encabezado,

        })

    return JsonResponse(contenedores_list, safe=False)



def get_efem_by_date(request, day, month):
    contenedores = Efemerides.objects.filter(fecha__day=day, fecha__month=month).order_by('fecha').values()
    contenedores_list = []

    for contenedor in contenedores:
        contenedores_list.append({
            'id': contenedor.id,
            'titulo': contenedor.titulo,
            'fecha': contenedor.fecha,
            'descripcion': contenedor.descripcion,
            'foto': contenedor.get_foto_url(),
            'color_de_fondo':contenedor.color_de_fondo,
            'encabezado':contenedor.encabezado,
        })

    return JsonResponse(contenedores_list, safe=False)



def get_acontecimiento_by_date(request, month, year):
    acontecimientos = Acontecimiento.objects.filter(fecha__month=month, fecha__year=year).order_by('fecha').values()
    acontecimientos_list = []

    for acontecimiento in acontecimientos:
        acontecimientos_list.append({
            'id': acontecimiento.id,
            'titulo': acontecimiento.titulo,
            'fecha': acontecimiento.fecha,
            'descripcion': acontecimiento.descripcion,
            'foto': acontecimiento.get_foto_url(),
            'color_de_fondo': acontecimiento.color_de_fondo,
            'encabezado': acontecimiento.encabezado,
        })

    return JsonResponse(acontecimientos_list, safe=False)

def get_evento_by_date(request, month, year):
    eventos = Evento.objects.filter(fecha__month=month, fecha__year=year).order_by('fecha').values()
    eventos_list = []

    for evento in eventos:
        eventos_list.append({
            'id': evento.id,
            'titulo': evento.titulo,
            'fecha': evento.fecha,
            'descripcion': evento.descripcion,
            'foto': evento.get_foto_url(),
            'color_de_fondo': evento.color_de_fondo,
            'encabezado': evento.encabezado,
            'hora': evento.hora,
        })

    return JsonResponse(eventos_list, safe=False)



def get_historia(request):
    historia = Historia.objects.all().values()
    contenedores_list = []

    for contenedor in historia:
        contenedores_list.append({
            'id': contenedor.id,
            'titulo': contenedor.titulo,
            'descripcion': contenedor.descripcion,
            'foto': contenedor.get_foto_url(),
            'color_de_fondo':contenedor.color_de_fondo,

        })

    return JsonResponse(contenedores_list, safe=False)

def get_centros_y_directores(request):
    centros_y_directores = Directores.objects.select_related('empresa').all().values()
    contenedores_list = []

    for contenedor in centros_y_directores:
        contenedores_list.append({
            'id': contenedor.id,
            'titulo': contenedor.titulo,
            'cargo': contenedor.cargo,
            'telefono': contenedor.télefono,
            'foto': contenedor.get_foto_url(),
            'consejo_de_direccion': contenedor.consejo_de_dirección,
            'color_de_fondo':contenedor.color_de_fondo,
            'empresa': str(contenedor.empresa.nombre),

        })

    return JsonResponse(contenedores_list, safe=False)

def get_premios(request):
    premios = Premio_Nacional_de_Música.objects.order_by('fecha').values()
    contenedores_list = []

    for contenedor in premios:
        contenedores_list.append({
            'id': contenedor.id,
            'titulo': contenedor.titulo,
            'descripcion': contenedor.descripcion,
            'bibliografia': contenedor.bibliografía,
            'foto': contenedor.get_foto_url(),
            'color_de_fondo':contenedor.color_de_fondo,
        })

    return JsonResponse(contenedores_list, safe=False)

def get_acontecimientos_semana(request):
    fecha = datetime.now()
    fecha_inicio = fecha - timedelta(days = fecha.weekday())
    fecha_fin = fecha_inicio + timedelta(days = 6)
    acontecimientos_semana = Acontecimiento.objects.filter(fecha__range = [fecha_inicio, fecha_fin]).order_by('fecha').values()
    acontecimientos_list = []

    for acontecimiento in acontecimientos_semana:
        acontecimientos_list.append({
            'id': acontecimiento.id,
            'titulo': acontecimiento.titulo,
            'fecha': acontecimiento.fecha,
            'descripcion': acontecimiento.descripcion,
            'foto': acontecimiento.get_foto_url(),
            'color_de_fondo': acontecimiento.color_de_fondo,
            'encabezado': acontecimiento.encabezado,
        })

    return JsonResponse(acontecimientos_list, safe=False)

def get_eventos_semana(request):
    fecha = datetime.now()
    fecha_inicio = fecha - timedelta(days = fecha.weekday())
    fecha_fin = fecha_inicio + timedelta(days = 6)
    eventos_semana = Evento.objects.filter(fecha__range = [fecha_inicio, fecha_fin]).order_by('fecha').values()
    eventos_list = []

    for evento in eventos_semana:
        eventos_list.append({
            'id': evento.id,
            'titulo': evento.titulo,
            'fecha': evento.fecha,
            'descripcion': evento.descripcion,
            'foto': evento.get_foto_url(),
            'color_de_fondo': evento.color_de_fondo,
            'encabezado': evento.encabezado,
            'hora': evento.hora,
        })

    return JsonResponse(eventos_list, safe=False)

def get_centros_contactos(request):
    centros = Centros_y_Empresas.objects.all().values()
    contenedores_list = []

    for contenedor in centros:
        contenedores_list.append({
            'id': contenedor.id,
            'titulo': contenedor.titulo,
            'telefono': contenedor.télefono,
            'foto': contenedor.get_foto_url(),
            'direccion': contenedor.dirección,
            'correo':contenedor.correo,


        })

    return JsonResponse(contenedores_list, safe=False)

# def get_directores_nombres(request):
#     directores = Directores.objects.all().values()
#     data = [
#         {
#             'nombre': director.nombre,

#         }
#         for director in directores
#     ]
#     return JsonResponse(data, safe=False)