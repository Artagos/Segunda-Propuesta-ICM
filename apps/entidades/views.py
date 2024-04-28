import json
from django.shortcuts import render
from django.db.models import Max
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, timedelta
from calendar import monthrange
from django.http import JsonResponse
from .models import Efemerides, Acontecimiento, Evento, Centros_y_Empresas, Directores, Redes,Historia_de_la_Institución, Multimedia, Premio_Nacional_de_Música, Iconos, Revista, BannerPrincipal, Podcast
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
from django.db.models.functions import ExtractMonth, ExtractDay, ExtractYear

from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


def select_banner_form(request):
    if request.method == 'POST':
        opcion = request.POST.get('opcion', '1')
        add_url = reverse('admin:entidades_bannerprincipal_add') + f'?opcion={opcion}'
        return HttpResponseRedirect(add_url)
    return render(request, 'select_form.html')

def lista_revistas(request):
    revistas = Revista.objects.all().order_by('-fecha').values()
    contenedores_list = []

    for contenedor in revistas:
        foto_url = ('https://back.dcubamusica.cult.cu/public/'+contenedor.get('imagen_portada') if contenedor.get('imagen_portada') else None)
        pdfurl = ('https://back.dcubamusica.cult.cu/public/'+contenedor.get('pdf') if contenedor.get('pdf') else None)

        contenedores_list.append({
            'id': contenedor['id'],
            'titulo': contenedor['titulo'],
            'descripcion': contenedor['descripcion'],
            'foto': foto_url,
            'pdf': pdfurl,
        })

    return JsonResponse(contenedores_list, safe=False)


def detalle_revista(request, id):
    # Intenta obtener los detalles de la revista como un diccionario dado un ID
    try:
        revista = Revista.objects.filter(id=id).values('id', 'titulo', 'descripcion', 'imagen_portada', 'pdf').get()
    except Revista.DoesNotExist:
        return JsonResponse({'error': 'Revista no encontrada'}, status=404)

    # Construye las URLs de las imágenes y pdfs, si existen
    foto_url = f'https://back.dcubamusica.cult.cu/public/{revista["imagen_portada"]}' if revista["imagen_portada"] else None
    pdf_url = f'https://back.dcubamusica.cult.cu/public/{revista["pdf"]}' if revista["pdf"] else None

    # Prepara el diccionario con los datos de la revista actualizados
    revista_data = {
        'id': revista['id'],
        'titulo': revista['titulo'],
        'descripcion': revista['descripcion'],
        'foto': foto_url,
        'pdf': pdf_url,
    }

    return JsonResponse(revista_data)



def lista_podcasts(request):
    podcasts = Podcast.objects.all().values()
    podcasts_data = []
    for contenedor in podcasts:
        foto_url = ('https://back.dcubamusica.cult.cu/public/'+contenedor.get('imagen_portada') if contenedor.get('imagen_portada') else None)

        podcasts_data.append({
            'id': contenedor['id'],
            'titulo': contenedor['titulo'],
            'descripcion': contenedor['descripcion'],
            'link_podcast': contenedor['link_podcast'],
            'foto': foto_url
        })
    return JsonResponse(podcasts_data, safe=False)

def get_banner_principal(request):

    for contenedor in BannerPrincipal.objects.all():
        contenedor.save()

    contenedores = BannerPrincipal.objects.all().order_by('numero_unico').values()
    contenedores_list = []

    for contenedor in contenedores:

        foto_url = ('https://back.dcubamusica.cult.cu/public/'+contenedor.get('foto') if contenedor.get('foto') else None)

        contenedor_dict = {
            'id': contenedor['id'],
            'tipo_contenedor': contenedor['tipo_contenedor'],
            # 'seleccionar_efemeride': contenedor['seleccionar_efemeride'] ,
            # 'seleccionar_acontecimiento': contenedor['seleccionar_acontecimiento'] ,
            # 'seleccionar_evento': contenedor['seleccionar_evento'],

            # 'seleccionar_efemeride': contenedor.get('seleccionar_efemeride'),  # Usa .get() para evitar KeyError
            # 'seleccionar_acontecimiento': contenedor.get('seleccionar_acontecimiento'),  # Usa .get()
            # 'seleccionar_evento': contenedor.get('seleccionar_evento'),  # Usa .get()

            'titulo': contenedor['titulo'],
            'descripcion': contenedor['descripcion'],
            'foto': foto_url,
            'color_de_fondo': contenedor['color_de_fondo'],
            'encabezado': contenedor['encabezado'],
            'numero_unico': contenedor['numero_unico'],
        }

        # if contenedor['tipo_contenedor'] == 'Efemeride':

        #     efemeride = Efemerides.objects.get(id=contenedor['seleccionar_efemeride_id'])
        #     foto_url = ('https://back.dcubamusica.cult.cu/public/'+efemeride.get('foto') if efemeride.get('foto') else None)


        #     contenedor_dict['titulo'] = efemeride.titulo
        #     contenedor_dict['descripcion'] = efemeride.descripcion
        #     contenedor_dict['foto'] = foto_url
        #     contenedor_dict['color_de_fondo'] = efemeride.color_de_fondo
        #     contenedor_dict['encabezado'] = efemeride.encabezado

        # elif contenedor['tipo_contenedor'] == 'Acontecimiento':
        #     acontecimiento = Acontecimiento.objects.get(id=contenedor['seleccionar_acontecimiento_id']).value()
        #     foto_url = ('https://back.dcubamusica.cult.cu/public/'+acontecimiento.get('foto') if acontecimiento.get('foto') else None)

        #     contenedor_dict['titulo'] = acontecimiento.titulo
        #     contenedor_dict['descripcion'] = acontecimiento.descripcion
        #     contenedor_dict['foto'] = foto_url
        #     contenedor_dict['color_de_fondo'] = acontecimiento.color_de_fondo
        #     contenedor_dict['encabezado'] = acontecimiento.encabezado
        #     contenedor_dict['enlace'] = evento.enlace

        # elif contenedor['tipo_contenedor'] =='Evento':
        #     evento = Evento.objects.get(id=contenedor['seleccionar_evento_id']).value()
        #     foto_url = ('https://back.dcubamusica.cult.cu/public/'+evento.get('foto') if evento.get('foto') else None)

        #     contenedor_dict['titulo'] = evento.titulo
        #     contenedor_dict['descripcion'] = evento.descripcion
        #     contenedor_dict['foto'] = foto_url
        #     contenedor_dict['color_de_fondo'] = evento.color_de_fondo
        #     contenedor_dict['encabezado'] = evento.encabezado
        #     contenedor_dict['enlace'] = evento.enlace
        #     contenedor_dict['hora'] = evento.hora

        contenedores_list.append(contenedor_dict)


    return JsonResponse(contenedores_list, safe=False)

def get_iconos(request):

    iconos_max_id = Iconos.objects.values('seccion').annotate(max_id=Max('id'))


    iconos_ids = [icono['max_id'] for icono in iconos_max_id]

    iconos_seleccionados = Iconos.objects.filter(id__in=iconos_ids)


    iconos_data = [
        {
            'seccion': icono.get_seccion_display(),
            'foto': 'https://back.dcubamusica.cult.cu' + icono.foto.url if icono.foto else None,


        }
        for icono in iconos_seleccionados
    ]

    return JsonResponse({'iconos': iconos_data})



def get_all_efem(request):
    contenedores = Efemerides.objects.all().order_by().values()
    contenedores_list = []



    for contenedor in contenedores:
        foto_url = ('https://back.dcubamusica.cult.cu/public/'+contenedor.get('foto') if contenedor.get('foto') else None)

        contenedores_list.append({
            'id': contenedor['id'],
            'titulo': contenedor['titulo'],
            'fecha': contenedor['fecha'],
            'descripcion': contenedor['descripcion'],
            'foto': foto_url,
            'color_de_fondo': contenedor['color_de_fondo'],
            'encabezado': contenedor['encabezado'],

        })

    return JsonResponse(contenedores_list, safe=False)



def get_efem_by_date(request, day, month):
    contenedores = Efemerides.objects.filter(fecha__day=day, fecha__month=month).order_by('fecha').values()
    contenedores_list = []

    for contenedor in contenedores:

        foto_url = ('https://back.dcubamusica.cult.cu/public/'+contenedor.get('foto') if contenedor.get('foto') else None)

        contenedores_list.append({
            'id': contenedor['id'],
            'titulo': contenedor['titulo'],
            'fecha': contenedor['fecha'],
            'descripcion': contenedor['descripcion'],
            'foto': foto_url,
            'color_de_fondo': contenedor['color_de_fondo'],
            'encabezado': contenedor['encabezado'],
        })

    return JsonResponse(contenedores_list, safe=False)

def get_efem_by_month(request, month):
    contenedores = Efemerides.objects.filter(fecha__month=month).order_by('fecha').values()
    contenedores_list = []

    for contenedor in contenedores:

        foto_url = ('https://back.dcubamusica.cult.cu/public/'+contenedor.get('foto') if contenedor.get('foto') else None)

        contenedores_list.append({
            'id': contenedor['id'],
            'titulo': contenedor['titulo'],
            'fecha': contenedor['fecha'],
            'descripcion': contenedor['descripcion'],
            'foto': foto_url,
            'color_de_fondo': contenedor['color_de_fondo'],
            'encabezado': contenedor['encabezado'],
        })

    return JsonResponse(contenedores_list, safe=False)



def get_acontecimiento_by_date(request, month, year):
    acontecimientos = Acontecimiento.objects.filter(fecha__month=month, fecha__year=year).order_by('fecha').values()
    acontecimientos_list = []

    for acontecimiento in acontecimientos:
        foto_url = ('https://back.dcubamusica.cult.cu/public/'+acontecimiento.get('foto') if acontecimiento.get('foto') else None)
        acontecimientos_list.append({
            'id': acontecimiento['id'],
            'titulo': acontecimiento['titulo'],
            'fecha': acontecimiento['fecha'],
            'descripcion': acontecimiento['descripcion'],
            'foto': foto_url,
            'color_de_fondo': acontecimiento['color_de_fondo'],
            'encabezado': acontecimiento['encabezado'],
        })

    return JsonResponse(acontecimientos_list, safe=False)

def get_evento_by_date(request, month, year):
    eventos = Evento.objects.filter(fecha__month=month, fecha__year=year).order_by('fecha').values()
    eventos_list = []

    for evento in eventos:
        foto_url = ('https://back.dcubamusica.cult.cu/public/'+evento.get('foto') if evento.get('foto') else None)
        eventos_list.append({
            'id': evento['id'],
            'titulo': evento['titulo'],
            'fecha': evento['fecha'],
            'descripcion': evento['descripcion'],
            'foto': foto_url,
            'color_de_fondo': evento['color_de_fondo'],
            'encabezado': evento['encabezado'],
            'hora': evento['hora'],
        })

    return JsonResponse(eventos_list, safe=False)



def get_historia(request):
    historia = Historia_de_la_Institución.objects.all().values()
    contenedores_list = []

    for contenedor in historia:
        foto_url = ('https://back.dcubamusica.cult.cu/public/'+contenedor.get('foto') if contenedor.get('foto') else None)
        contenedores_list.append({
            'id': contenedor['id'],
            'titulo': contenedor['titulo'],
            'descripcion': contenedor['descripcion'],
            'foto': foto_url,
            'color_de_fondo': contenedor['color_de_fondo'],

        })

    return JsonResponse(contenedores_list, safe=False)

def get_centros_y_directores(request):
    # Se especifican los campos de la empresa con la sintaxis 'empresa__campo'
    centros_y_directores = Directores.objects.select_related('empresa').all().values(
        # 'id', 'nombre', 'telefono', 'consejo_de_direccion', 'foto', 'cargo',
        # 'empresa__nombre',  # Por ejemplo, si la empresa tiene un campo 'nombre'
        # 'es_cto', 'es_ceo'
    )
    contenedores_list = []

    for contenedor in centros_y_directores:
        foto_url = f'https://back.dcubamusica.cult.cu/public/{contenedor.get("foto")}' if contenedor.get('foto') else None
        # Si la empresa no es None, obtiene el nombre limpio del campo RichTextField
        # if contenedor.get('empresa__nombre'):
        #     empresa_nombre = strip_tags(contenedor['empresa__nombre'])
        # else:
        #     empresa_nombre = 'Sin empresa'

        empresa_nombre = contenedor.get('empresa_id')

        contenedores_list.append({
            'id': contenedor['id'],
            'nombre': contenedor['nombre'],
            'telefono': contenedor.get('télefono'),
            'consejo_de_direccion': contenedor['consejo_de_dirección'],
            'foto': foto_url,
            'cargo': contenedor['cargo'],
            'empresa': empresa_nombre,
            'cto': contenedor.get('es_cto', False),
            'ceo': contenedor.get('es_ceo', False),
        })

    return JsonResponse(contenedores_list, safe=False)


def get_premios(request):
    premios = Premio_Nacional_de_Música.objects.order_by('-año').values()
    contenedores_list = []

    for contenedor in premios:
        foto_url = ('https://back.dcubamusica.cult.cu/public/'+contenedor.get('foto') if contenedor.get('foto') else None)
        contenedores_list.append({

            'id': contenedor['id'],
            'titulo': contenedor['titulo'],
            'descripcion': contenedor['descripcion'],
            'foto': foto_url,
            'año' : contenedor['año'],
            'color_de_fondo': contenedor['color_de_fondo'],
            'bibliografia': contenedor['bibliografía'],
        })

    return JsonResponse(contenedores_list, safe=False)

def get_acontecimientos_semana(request):
    fecha = datetime.now()
    fecha_inicio = fecha - timedelta(days = fecha.weekday())
    fecha_fin = fecha_inicio + timedelta(days = 6)
    acontecimientos_semana = Acontecimiento.objects.filter(fecha__range = [fecha_inicio, fecha_fin]).order_by('fecha').values()
    acontecimientos_list = []

    for acontecimiento in acontecimientos_semana:
        foto_url = ('https://back.dcubamusica.cult.cu/public/'+acontecimiento.get('foto') if acontecimiento.get('foto') else None)
        acontecimientos_list.append({
            'id': acontecimiento['id'],
            'titulo': acontecimiento['titulo'],
            'fecha': acontecimiento['fecha'],
            'descripcion': acontecimiento['descripcion'],
            'foto': foto_url,
            'color_de_fondo': acontecimiento['color_de_fondo'],
            'encabezado': acontecimiento['encabezado'],
        })

    return JsonResponse(acontecimientos_list, safe=False)

def get_eventos_semana(request):
    fecha = datetime.now()
    fecha_inicio = fecha - timedelta(days = fecha.weekday())
    fecha_fin = fecha_inicio + timedelta(days = 6)
    eventos_semana = Evento.objects.filter(fecha__range = [fecha_inicio, fecha_fin]).order_by('fecha').values()
    eventos_list = []

    for evento in eventos_semana:
        foto_url = ('https://back.dcubamusica.cult.cu/public/'+evento.get('foto') if evento.get('foto') else None)
        eventos_list.append({
            'id': evento['id'],
            'titulo': evento['titulo'],
            'fecha': evento['fecha'],
            'descripcion': evento['descripcion'],
            'foto': foto_url,
            'color_de_fondo': evento['color_de_fondo'],
            'encabezado': evento['encabezado'],
            'hora': evento['hora'],
        })

    return JsonResponse(eventos_list, safe=False)

def get_centros_contactos(request):
    centros = Centros_y_Empresas.objects.all().values()
    contenedores_list = []

    for contenedor in centros:
        foto_url = ('https://back.dcubamusica.cult.cu/public/'+contenedor.get('foto') if contenedor.get('foto') else None)
        contenedores_list.append({
            'id': contenedor['id'],
            'nombre': contenedor['nombre'],
            'telefono': contenedor['télefono'],
            'direccion': contenedor['dirección'],
            'foto': foto_url,
            'correo': contenedor['correo'],



        })

    return JsonResponse(contenedores_list, safe=False)


def get_redes(request):
    # Se especifican los campos de la empresa con la sintaxis 'empresa__campo'
    redes = Redes.objects.all().values(
    )
    contenedores_list = []

    for contenedor in redes:
        foto_url = f'https://back.dcubamusica.cult.cu/public/{contenedor.get("foto")}' if contenedor.get('foto') else None

        contenedores_list.append({
            'id': contenedor['id'],
            'titulo': contenedor['titulo'],
            'enlace': contenedor['enlace'],
            'foto': foto_url,

        })

    return JsonResponse(contenedores_list, safe=False)

def get_multimedias(request):
    # Se especifican los campos de la empresa con la sintaxis 'empresa__campo'
    multimedias = Multimedia.objects.all().values(
    )
    contenedores_list = []

    for contenedor in multimedias:
        foto_url = f'https://back.dcubamusica.cult.cu/public/{contenedor.get("foto")}' if contenedor.get('foto') else None
        multimedia = ('https://back.dcubamusica.cult.cu/public/'+contenedor.get('archivo') if contenedor.get('archivo') else None)

        # Si la empresa no es None, obtiene el nombre limpio del campo RichTextField
        # if contenedor.get('empresa__nombre'):
        #     empresa_nombre = strip_tags(contenedor['empresa__nombre'])
        # else:
        #     empresa_nombre = 'Sin empresa'
        contenedores_list.append({
            'id': contenedor['id'],
            'titulo': contenedor['titulo'],
            'tipo': contenedor.get('tipo'),
            'enlace': contenedor['enlace'],
            'foto': foto_url,
            'archivo': multimedia,
            'descripcion': contenedor['descripcion'],
            'color_de_fondo': contenedor['color_de_fondo'],

        })

    return JsonResponse(contenedores_list, safe=False)


def detalle_multimedia(request, id):
    # Intenta obtener los detalles de la revista como un diccionario dado un ID
    try:
        contenedor = Multimedia.objects.filter(id=id).values().get()
    except Multimedia.DoesNotExist:
        return JsonResponse({'error': 'Multimedia no encontrada'}, status=404)

    # Construye las URLs de las imágenes y pdfs, si existen
    foto_url = f'https://back.dcubamusica.cult.cu/public/{contenedor.get("foto")}' if contenedor.get('foto') else None

    multimedia = ('https://back.dcubamusica.cult.cu/public/'+contenedor.get('archivo') if contenedor.get('archivo') else None)

    # Prepara el diccionario con los datos de la revista actualizados
    mult = {
        'id': contenedor['id'],
        'titulo': contenedor['titulo'],
        'tipo': contenedor.get('tipo'),
        'enlace': contenedor['enlace'],
        'foto': foto_url,
        'archivo': multimedia,
        'descripcion': contenedor['descripcion'],
        'color_de_fondo': contenedor['color_de_fondo'],
    }

    return JsonResponse(mult)
