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
from django.utils.translation import activate
from django.utils.translation import get_language
from django.utils import translation



def select_banner_form(request):
    if request.method == 'POST':
        opcion = request.POST.get('opcion', '1')
        add_url = reverse('admin:entidades_bannerprincipal_add') + f'?opcion={opcion}'
        return HttpResponseRedirect(add_url)
    return render(request, 'select_form.html')

def lista_revistas(request):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        titulo_field = f'titulo_{current_language}'
        descripcion_field = f'descripcion_{current_language}'

        revistas = Revista.objects.all().order_by('-fecha').values(
            'id', titulo_field, descripcion_field, 'imagen_portada', 'pdf'
        )
        contenedores_list = []
        for contenedor in revistas:
            foto_url = 'https://back.dcubamusica.cult.cu/public/' + contenedor.get('imagen_portada', '')
            pdf_url = 'https://back.dcubamusica.cult.cu/public/' + contenedor.get('pdf', '')
            titulo = contenedor.get(titulo_field, 'Sin título')  # Fallback si falta la traducción
            descripcion = contenedor.get(descripcion_field, 'Sin descripción')

            if titulo is None:
                continue
            contenedores_list.append({
                'id': contenedor['id'],
                'titulo': titulo,
                'descripcion': descripcion,
                'foto': foto_url,
                'pdf': pdf_url,
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

# def lista_podcasts(request):
#     # Obtener el idioma actual
#     current_language = get_language()

#     # Obtener los podcasts en el idioma actual
#     podcasts = Podcast.objects.all()
#     podcasts_data = []

#     for podcast in podcasts:
#         # Suponiendo que 'titulo' y 'descripcion' son campos traducidos
#         titulo = getattr(podcast, f'titulo_{current_language}', podcast.titulo)
#         descripcion = getattr(podcast, f'descripcion_{current_language}', podcast.descripcion)

#         podcasts_data.append({
#             'id': podcast.id,
#             'titulo': titulo,
#             'descripcion': descripcion,
#             'link_podcast': podcast.link_podcast,
#             'foto': podcast.get_foto_url()
#         })

#     return JsonResponse(podcasts_data, safe=False)


def lista_podcasts(request):
    # Obtener el idioma desde la URL o utilizar 'en' como predeterminado
    lang = request.GET.get('lang', 'en')

    # Activar temporalmente el idioma especificado
    with translation.override(lang):
        # Obtener el idioma actual activo
        current_language = translation.get_language()

        # Preparar nombres de campo con sufijo de idioma
        titulo_field = f'titulo_{current_language}'
        descripcion_field = f'descripcion_{current_language}'

        # Utilizar .values() especificando los campos de traducción
        podcasts = Podcast.objects.all().values(
            'id', 'link_podcast', 'foto', titulo_field, descripcion_field
        )

        podcasts_data = []
        for contenedor in podcasts:
            foto_url = 'https://back.dcubamusica.cult.cu/public/' + contenedor.get('foto', '')

            # Acceder directamente a los campos traducidos
            titulo = contenedor.get(titulo_field, 'Sin título')  # Fallback si falta la traducción
            descripcion = contenedor.get(descripcion_field, 'Sin descripción')

            if titulo is None:
                continue

            podcasts_data.append({
                'id': contenedor['id'],
                'titulo': titulo,
                'descripcion': descripcion,
                'link_podcast': contenedor['link_podcast'],
                'foto': foto_url
            })

    return JsonResponse(podcasts_data, safe=False)

def get_banner_principal(request):
    # Obtener el idioma desde la URL o utilizar 'es' como predeterminado
    lang = request.GET.get('lang', 'es')

    # Activar temporalmente el idioma especificado
    with translation.override(lang):
        current_language = translation.get_language()
        titulo_field = f'titulo_{current_language}'
        descripcion_field = f'descripcion_{current_language}'
        encabezado_field = f'encabezado_{current_language}'

        # Actualizar todas las instancias para asegurar que los datos son actuales
        for contenedor in BannerPrincipal.objects.all():
            contenedor.save()

        # Obtener los banners
        banners = BannerPrincipal.objects.all().order_by('numero_unico').values(
            'id', 'tipo_contenedor', 'seleccionar_efemeride_id', 'seleccionar_acontecimiento_id',
            'seleccionar_evento_id', titulo_field, descripcion_field, encabezado_field,
            'foto', 'color_de_fondo', 'numero_unico'
        )

        banners_data = []
        for banner in banners:
            foto_url = 'https://back.dcubamusica.cult.cu/public/' + banner.get('foto', '')
            titulo = banner.get(titulo_field, 'Sin título')  # Fallback si falta la traducción
            descripcion = banner.get(descripcion_field, 'Sin descripción')
            encabezado = banner.get(encabezado_field, 'Sin encabezado')

            if titulo is None:
                continue

            banner_dict = {
                'id': banner['id'],
                'tipo_contenedor': banner['tipo_contenedor'],
                'titulo':titulo,
                'descripcion': descripcion,
                'encabezado': encabezado,
                'foto': foto_url,
                'color_de_fondo': banner['color_de_fondo'],
                'numero_unico': banner['numero_unico'],
            }
            banners_data.append(banner_dict)

        return JsonResponse(banners_data, safe=False)


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
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        titulo_field = f'titulo_{current_language}'
        descripcion_field = f'descripcion_{current_language}'
        encabezado_field = f'encabezado_{current_language}'


        efemerides = Efemerides.objects.all().order_by().values(
            'id', 'fecha', 'foto', 'color_de_fondo', encabezado_field, titulo_field, descripcion_field
        )

        efemerides_list = []
        for efemeride in efemerides:
            titulo = efemeride.get(titulo_field, 'Sin título')
            descripcion = efemeride.get(descripcion_field, 'Sin descripción')
            if titulo is None:
                continue

            efemerides_list.append({
                'id': efemeride['id'],
                'titulo': titulo,
                'fecha': efemeride['fecha'],
                'descripcion': descripcion,
                'foto': 'https://back.dcubamusica.cult.cu/public/' + efemeride.get('foto', ''),
                'color_de_fondo': efemeride['color_de_fondo'],
                'encabezado': efemeride.get(encabezado_field, '')
            })

    return JsonResponse(efemerides_list, safe=False)



def get_efem_by_date(request, day, month):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        titulo_field = f'titulo_{current_language}'
        descripcion_field = f'descripcion_{current_language}'
        encabezado_field = f'encabezado_{current_language}'


        efemerides = Efemerides.objects.filter(fecha__day=day, fecha__month=month).order_by('fecha').values(
            'id', 'fecha', 'foto', 'color_de_fondo', encabezado_field, titulo_field, descripcion_field
        )

        efemerides_list = []
        for efemeride in efemerides:
            titulo = efemeride.get(titulo_field, 'Sin título')
            descripcion = efemeride.get(descripcion_field, 'Sin descripción')
            if titulo is None:
                continue

            efemerides_list.append({
                'id': efemeride['id'],
                'titulo': titulo,
                'fecha': efemeride['fecha'],
                'descripcion': descripcion,
                'foto': 'https://back.dcubamusica.cult.cu/public/' + efemeride.get('foto', ''),
                'color_de_fondo': efemeride['color_de_fondo'],
                'encabezado': efemeride.get(encabezado_field, '')
            })

    return JsonResponse(efemerides_list, safe=False)


def get_efem_by_month(request, month):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        titulo_field = f'titulo_{current_language}'
        descripcion_field = f'descripcion_{current_language}'
        encabezado_field = f'encabezado_{current_language}'


        efemerides = Efemerides.objects.filter(fecha__month=month).order_by('fecha').values(
            'id', 'fecha', 'foto', 'color_de_fondo', encabezado_field, titulo_field, descripcion_field
        )

        efemerides_list = []
        for efemeride in efemerides:
            titulo = efemeride.get(titulo_field, 'Sin título')
            descripcion = efemeride.get(descripcion_field, 'Sin descripción')
            if titulo is None:
                continue

            efemerides_list.append({
                'id': efemeride['id'],
                'titulo': titulo,
                'fecha': efemeride['fecha'],
                'descripcion': descripcion,
                'foto': 'https://back.dcubamusica.cult.cu/public/' + efemeride.get('foto', ''),
                'color_de_fondo': efemeride['color_de_fondo'],
                'encabezado': efemeride.get(encabezado_field, '')
            })

    return JsonResponse(efemerides_list, safe=False)




def get_acontecimiento_by_date(request, month, year):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        titulo_field = f'titulo_{current_language}'
        descripcion_field = f'descripcion_{current_language}'
        encabezado_field = f'encabezado_{current_language}'

        acontecimientos = Acontecimiento.objects.filter(fecha__month=month, fecha__year=year).order_by('fecha').values(
            'id', 'fecha', 'foto', 'color_de_fondo', titulo_field, descripcion_field, encabezado_field
        )

        acontecimientos_list = []
        for acontecimiento in acontecimientos:
            titulo = acontecimiento.get(titulo_field, 'Sin título')
            descripcion = acontecimiento.get(descripcion_field, 'Sin descripción')
            encabezado = acontecimiento.get(encabezado_field, '')

            if titulo is None:
                continue

            acontecimientos_list.append({
                'id': acontecimiento['id'],
                'titulo': titulo,
                'fecha': acontecimiento['fecha'],
                'descripcion': descripcion,
                'foto': 'https://back.dcubamusica.cult.cu/public/' + acontecimiento.get('foto', ''),
                'color_de_fondo': acontecimiento['color_de_fondo'],
                'encabezado': encabezado,
            })

    return JsonResponse(acontecimientos_list, safe=False)


def get_evento_by_date(request, month, year):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        titulo_field = f'titulo_{current_language}'
        descripcion_field = f'descripcion_{current_language}'
        encabezado_field = f'encabezado_{current_language}'

        eventos = Evento.objects.filter(fecha__month=month, fecha__year=year).order_by('fecha').values(
            'id', 'fecha', 'foto', 'color_de_fondo', 'hora', titulo_field, descripcion_field, encabezado_field
        )

        eventos_list = []
        for evento in eventos:
            titulo = evento.get(titulo_field, 'Sin título')
            descripcion = evento.get(descripcion_field, 'Sin descripción')
            encabezado = evento.get(encabezado_field, '')

            if titulo is None:
                continue


            eventos_list.append({
                'id': evento['id'],
                'titulo': titulo,
                'fecha': evento['fecha'],
                'descripcion': descripcion,
                'foto': 'https://back.dcubamusica.cult.cu/public/' + evento.get('foto', ''),
                'color_de_fondo': evento['color_de_fondo'],
                'encabezado': encabezado,
                'hora': evento['hora'],
            })



    return JsonResponse(eventos_list, safe=False)



def get_historia(request):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        titulo_field = f'titulo_{current_language}'
        descripcion_field = f'descripcion_{current_language}'

        historias = Historia_de_la_Institución.objects.all().values(
            'id', 'foto', 'color_de_fondo', titulo_field, descripcion_field
        )

        historias_list = []
        for historia in historias:
            titulo = historia.get(titulo_field, 'Sin título')
            descripcion = historia.get(descripcion_field, 'Sin descripción')

            if titulo is None:
                continue

            historias_list.append({
                'id': historia['id'],
                'titulo': titulo,
                'descripcion': descripcion,
                'foto': 'https://back.dcubamusica.cult.cu/public/' + historia.get('foto', ''),
                'color_de_fondo': historia['color_de_fondo'],
            })

    return JsonResponse(historias_list, safe=False)

def get_centros_y_directores(request):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        nombre_field = f'nombre_{current_language}'
        cargo_field = f'cargo_{current_language}'

        centros_y_directores = Directores.objects.select_related('empresa').all().values(
            'id', 'télefono', 'consejo_de_dirección', 'foto', 'es_cto', 'es_ceo',
            nombre_field, cargo_field, 'empresa_id'
        )
        contenedores_list = []
        for contenedor in centros_y_directores:
            nombre = contenedor.get(nombre_field, 'Nombre no disponible')
            cargo = contenedor.get(cargo_field, 'Cargo no disponible')
            empresa_nombre = contenedor.get('empresa_id')
            foto_url = f'https://back.dcubamusica.cult.cu/public/{contenedor.get("foto")}' if contenedor.get('foto') else None

            if nombre is None:
                continue

            contenedores_list.append({
                'id': contenedor['id'],
                'nombre': nombre,
                'telefono': contenedor.get('télefono'),
                'consejo_de_direccion': contenedor['consejo_de_dirección'],
                'foto': foto_url,
                'cargo': cargo,
                'empresa': empresa_nombre,
                'cto': contenedor.get('es_cto', False),
                'ceo': contenedor.get('es_ceo', False),
            })

    return JsonResponse(contenedores_list, safe=False)


def get_premios(request):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        titulo_field = f'titulo_{current_language}'
        descripcion_field = f'descripcion_{current_language}'

        premios = Premio_Nacional_de_Música.objects.order_by('-año').values(
            'id', 'año', 'foto', 'color_de_fondo', 'bibliografía', titulo_field, descripcion_field
        )

        premios_list = []
        for premio in premios:
            titulo = premio.get(titulo_field)
            descripcion = premio.get(descripcion_field, 'Sin descripción')

            if titulo is None:
                continue

            descripcion = premio.get(descripcion_field, 'Sin descripción')
            premios_list.append({
                'id': premio['id'],
                'titulo': titulo,
                'descripcion': descripcion,
                'foto': 'https://back.dcubamusica.cult.cu/public/'+premio.get('foto', ''),
                'año': premio['año'],
                'color_de_fondo': premio['color_de_fondo'],
                'bibliografia': premio['bibliografía'],
            })

    return JsonResponse(premios_list, safe=False)

def get_acontecimientos_semana(request):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        titulo_field = f'titulo_{current_language}'
        descripcion_field = f'descripcion_{current_language}'
        encabezado_field = f'encabezado_{current_language}'

        fecha = datetime.now()
        fecha_inicio = fecha - timedelta(days=fecha.weekday())
        fecha_fin = fecha_inicio + timedelta(days=6)
        acontecimientos_semana = Acontecimiento.objects.filter(fecha__range=[fecha_inicio, fecha_fin]).order_by('fecha').values(
            'id', 'fecha', 'foto', 'color_de_fondo', encabezado_field, titulo_field, descripcion_field
        )

        acontecimientos_list = []
        for acontecimiento in acontecimientos_semana:
            titulo = acontecimiento.get(titulo_field, 'Sin título')
            descripcion = acontecimiento.get(descripcion_field, 'Sin descripción')


            if titulo is None:
                continue

            acontecimientos_list.append({
                'id': acontecimiento['id'],
                'titulo': titulo,
                'fecha': acontecimiento['fecha'],
                'descripcion': descripcion,
                'foto': 'https://back.dcubamusica.cult.cu/public/' + acontecimiento.get('foto', ''),
                'color_de_fondo': acontecimiento['color_de_fondo'],
                'encabezado': acontecimiento.get(encabezado_field, '')
            })

    return JsonResponse(acontecimientos_list, safe=False)


def get_eventos_semana(request):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        titulo_field = f'titulo_{current_language}'
        descripcion_field = f'descripcion_{current_language}'
        encabezado_field = f'encabezado_{current_language}'

        fecha = datetime.now()
        fecha_inicio = fecha - timedelta(days=fecha.weekday())
        fecha_fin = fecha_inicio + timedelta(days=6)
        eventos_semana = Evento.objects.filter(fecha__range=[fecha_inicio, fecha_fin]).order_by('fecha').values(
            'id', 'fecha', 'foto', 'color_de_fondo', encabezado_field, 'hora', titulo_field, descripcion_field
        )

        eventos_list = []
        for evento in eventos_semana:
            titulo = evento.get(titulo_field, 'Sin título')
            descripcion = evento.get(descripcion_field, 'Sin descripción')

            if titulo is None:
                continue
            eventos_list.append({
                'id': evento['id'],
                'titulo': titulo,
                'fecha': evento['fecha'],
                'descripcion': descripcion,
                'foto': 'https://back.dcubamusica.cult.cu/public/' + evento.get('foto', ''),
                'color_de_fondo': evento['color_de_fondo'],
                'encabezado': evento.get(encabezado_field, ''),
                'hora': evento.get('hora', '')
            })

    return JsonResponse(eventos_list, safe=False)


def get_centros_contactos(request):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        nombre_field = f'nombre_{current_language}'
        direccion_field = f'dirección_{current_language}'

        centros = Centros_y_Empresas.objects.all().values(
            'id', 'télefono', 'correo', nombre_field, direccion_field
        )
        contenedores_list = []
        for contenedor in centros:
            nombre = contenedor.get(nombre_field, 'Nombre no disponible')
            direccion = contenedor.get(direccion_field, 'Dirección no disponible')
            if nombre is None:
                continue
            contenedores_list.append({
                'id': contenedor['id'],
                'nombre': nombre,
                'telefono': contenedor['télefono'],
                'direccion': direccion,
                'correo': contenedor['correo']
            })

    return JsonResponse(contenedores_list, safe=False)



def get_redes(request):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        titulo_field = f'titulo_{current_language}'

        redes = Redes.objects.all().values('id', 'enlace', 'foto', titulo_field)

        redes_list = []
        for red in redes:
            titulo = red.get(titulo_field, 'Sin título')

            if titulo is None:
                continue

            redes_list.append({
                'id': red['id'],
                'titulo': titulo,
                'enlace': red['enlace'],
                'foto': 'https://back.dcubamusica.cult.cu/public/' + red.get('foto', ''),
            })

    return JsonResponse(redes_list, safe=False)

def get_multimedias(request):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        titulo_field = f'titulo_{current_language}'
        descripcion_field = f'descripcion_{current_language}'

        multimedias = Multimedia.objects.all().values(
            'id', 'tipo', 'enlace', 'archivo', 'foto', titulo_field, descripcion_field, 'color_de_fondo'
        )

        multimedias_list = []
        for multimedia in multimedias:
            titulo = multimedia.get(titulo_field)
            descripcion = multimedia.get(descripcion_field, 'Sin descripción')

            if titulo is None:
                continue

            multimedias_list.append({
                'id': multimedia['id'],
                'titulo': titulo,
                'descripcion': descripcion,
                'tipo': multimedia['tipo'],
                'enlace': multimedia['enlace'],
                'foto': 'https://back.dcubamusica.cult.cu/public/' + multimedia.get('foto', ''),
                'archivo': 'https://back.dcubamusica.cult.cu/public/' + multimedia.get('archivo', ''),
                'color_de_fondo': multimedia['color_de_fondo'],
            })

    return JsonResponse(multimedias_list, safe=False)


# def detalle_multimedia(request, id):
#     # Intenta obtener los detalles de la revista como un diccionario dado un ID
#     try:
#         contenedor = Multimedia.objects.filter(id=id).values().get()
#     except Multimedia.DoesNotExist:
#         return JsonResponse({'error': 'Multimedia no encontrada'}, status=404)

#     # Construye las URLs de las imágenes y pdfs, si existen
#     foto_url = f'https://back.dcubamusica.cult.cu/public/{contenedor.get("foto")}' if contenedor.get('foto') else None

#     multimedia = ('https://back.dcubamusica.cult.cu/public/'+contenedor.get('archivo') if contenedor.get('archivo') else None)

#     # Prepara el diccionario con los datos de la revista actualizados
#     mult = {
#         'id': contenedor['id'],
#         'titulo': contenedor['titulo'],
#         'tipo': contenedor.get('tipo'),
#         'enlace': contenedor['enlace'],
#         'foto': foto_url,
#         'archivo': multimedia,
#         'descripcion': contenedor['descripcion'],
#         'color_de_fondo': contenedor['color_de_fondo'],
#     }

#     return JsonResponse(mult)


def detalle_multimedia(request, id):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        titulo_field = f'titulo_{current_language}'
        descripcion_field = f'descripcion_{current_language}'

        try:
            contenedor = Multimedia.objects.filter(id=id).values('id', 'foto', 'archivo', 'tipo', 'enlace', 'color_de_fondo', titulo_field, descripcion_field).get()
        except Multimedia.DoesNotExist:
            return JsonResponse({'error': 'Multimedia no encontrada'}, status=404)

        foto_url = f'https://back.dcubamusica.cult.cu/public/{contenedor.get("foto")}' if contenedor.get('foto') else None
        multimedia_url = f'https://back.dcubamusica.cult.cu/public/{contenedor.get("archivo")}' if contenedor.get('archivo') else None
        titulo = contenedor.get(titulo_field, 'Sin título')
        descripcion = contenedor.get(descripcion_field, 'Sin descripción')

        multimedia_data = {
            'id': contenedor['id'],
            'titulo': titulo,
            'tipo': contenedor.get('tipo'),
            'enlace': contenedor['enlace'],
            'foto': foto_url,
            'archivo': multimedia_url,
            'descripcion': descripcion,
            'color_de_fondo': contenedor['color_de_fondo'],
        }

    return JsonResponse(multimedia_data)



def get_ceo(request):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        name_field = f'nombre_{current_language}'
        position_field = f'cargo_{current_language}'

        ceo = Directores.objects.filter(es_ceo=True).values(name_field, position_field).first()
        if ceo is None:
            return JsonResponse({'error': 'No CEO found'}, status=404)

        name = ceo.get(name_field, 'No name available')
        position = ceo.get(position_field, 'No position available')

        if name is None:
            return JsonResponse({'error': 'No CTO found'}, status=404)

        return JsonResponse({'nombre': name, 'cargo': position})

def get_cto(request):
    lang = request.GET.get('lang', 'es')
    with translation.override(lang):
        current_language = translation.get_language()
        name_field = f'nombre_{current_language}'
        position_field = f'cargo_{current_language}'

        cto = Directores.objects.filter(es_cto=True).values(name_field, position_field).first()
        if cto is None:
            return JsonResponse({'error': 'No CTO found'}, status=404)

        name = cto.get(name_field, 'No name available')
        position = cto.get(position_field, 'No position available')

        if name is None:
            return JsonResponse({'error': 'No CTO found'}, status=404)

        return JsonResponse({'nombre': name, 'cargo': position})

# def get_cto(request):
#     cto = Director.objects.filter(position='es_cto').first()
#     if cto is None:
#         return JsonResponse({'error': 'No CTO found'}, status=404)
#     return JsonResponse({'name': cto.name, 'position': cto.position})