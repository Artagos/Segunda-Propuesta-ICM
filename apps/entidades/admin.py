from django.contrib import admin
from .models import Efemerides, Acontecimiento, Evento, Centros_y_Empresas, Directores, Historia_de_la_Institución, Multimedia, Premio_Nacional_de_Música
from .models import BannerPrincipal, Iconos, Revista, Podcast ,Redes#ContenedorConFondo, ContenedorConFondoSoloTitulo, ContenedorICM,
from django import forms
from django.utils.html import strip_tags
from .forms import BannerPrincipalForm1, BannerPrincipalForm2, OpcionesForm
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.urls import reverse
import datetime
from django.contrib.admin import SimpleListFilter
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError



class RichTextFieldAdmin(admin.ModelAdmin):
    def get_titulo_plain(self, obj):
        return strip_tags(obj.titulo)
    get_titulo_plain.short_description = 'Título'

    def get_desc_plain(self, obj):
        return strip_tags(obj.descripcion)
    get_desc_plain.short_description = 'Descripción'


@admin.register(Revista)
class RevistaAdmin(RichTextFieldAdmin):
    list_display = ('get_titulo_plain', 'get_desc_plain', 'fecha','pdf', 'imagen_portada')

class PodcastAdminForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        link_podcast = cleaned_data.get('link_podcast')
        archivo_local = cleaned_data.get('archivo_local')

        # Verificar que solo uno de los dos campos esté lleno
        if bool(link_podcast) == bool(archivo_local):  # Ambos son True o ambos son False
            raise ValidationError('Debes llenar exactamente uno de los campos: link_podcast o archivo_local.')

        return cleaned_data

@admin.register(Podcast)
class PodcastAdmin(RichTextFieldAdmin):
    form = PodcastAdminForm
    list_display = ('get_titulo_plain', 'get_desc_plain', 'link_podcast', 'archivo_local')

@admin.register(BannerPrincipal)
class BannerPrincipalAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'encabezado', 'descripcion', 'foto', 'color_de_fondo', 'numero_unico', 'seleccionar_efemeride', 'seleccionar_acontecimiento', 'seleccionar_evento')

    def get_form(self, request, obj=None, **kwargs):
        # Obtiene la opción de la URL
        opcion = request.GET.get('opcion', '1')  # Opción por defecto es '1'

        if opcion == '1':
            form_class = BannerPrincipalForm1
            # Define las opciones para el tipo de contenedor específicas para Form1
            tipo_contenedor_choices = [
                ('ContenedorConFondo', 'Tipo 1'),
                ('ContenedorConFondoSoloTitulo', 'Tipo 2'),
                ('ContenedorICM', 'Tipo 3'),
                        # Supongamos que solo quieres esta opción para el Form1
            ]
        elif opcion == '2':
            form_class = BannerPrincipalForm2
            # Define las opciones para el tipo de contenedor específicas para Form2
            tipo_contenedor_choices = [
                ('Evento', 'Contenedor: Evento'),
                ('Acontecimiento', 'Contenedor: Acontecimiento'),
                ('Efemeride', 'Contenedor: Efemeride'),
            ]
        else:
            form_class = BannerPrincipalForm1  # Por defecto usar formulario 1 si la opción no es válida
            tipo_contenedor_choices = []

        Form = super().get_form(request, obj, form=form_class, **kwargs)

        # Configura las opciones de tipo_contenedor según la opción seleccionada
        Form.base_fields['tipo_contenedor'].choices = tipo_contenedor_choices

        # Establece los campos como no requeridos basados en la opción
        if opcion == '2':
            for field_name in ['seleccionar_efemeride', 'seleccionar_acontecimiento', 'seleccionar_evento']:
                Form.base_fields[field_name].required = False
        elif opcion == '1':
            for field_name in ['titulo', 'encabezado', 'descripcion', 'foto', 'color_de_fondo']:
                Form.base_fields[field_name].required = False

        return Form

    def add_view(self, request, form_url='', extra_context=None):
            if 'opcion' not in request.GET:
                # Redirigir al usuario a una página de selección de opciones
                select_url = reverse('entidades:bannerprincipal_select')
                return HttpResponseRedirect(select_url)
            return super().add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        # Añadir la opción a extra_context para usarla en la plantilla si es necesario
        extra_context = extra_context or {}
        if 'opcion' in request.GET:
            extra_context['opcion'] = request.GET['opcion']
        return super().change_view(request, object_id, form_url, extra_context)


@admin.register(Iconos)
class IconosAdmin(admin.ModelAdmin):
    list_display = ('seccion', 'foto')

@admin.register(Evento)
class EventoAdmin(RichTextFieldAdmin):
    list_display = ('get_titulo_plain', 'fecha', 'get_desc_plain', 'enlace', 'hora', 'color_de_fondo', 'foto')

@admin.register(Historia_de_la_Institución)
class HistoriaAdmin(RichTextFieldAdmin):
    list_display = ('get_titulo_plain', 'get_desc_plain', 'foto', 'color_de_fondo')

@admin.register(Centros_y_Empresas)
class CentrosAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dirección', 'télefono', 'correo')

class DirectoresAdminForm(forms.ModelForm):
    class Meta:
        model = Directores
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        es_ceo = cleaned_data.get('es_ceo')
        es_cto = cleaned_data.get('es_cto')

        if es_ceo and es_cto:
            raise ValidationError('Un director no puede ser marcado como CEO y CTO al mismo tiempo.')

        return cleaned_data

@admin.register(Directores)
class DirectoresAdmin(admin.ModelAdmin):
    form = DirectoresAdminForm
    list_display = ('nombre', 'cargo', 'télefono', 'correo', 'consejo_de_dirección', 'empresa', 'foto', 'es_ceo','es_cto')


class PremioForm(forms.ModelForm):
    current_year = datetime.datetime.now().year
    year_choices = [(year, year) for year in range(1997, current_year + 1)]
    año = forms.ChoiceField(choices=year_choices)

    class Meta:
        model = Premio_Nacional_de_Música
        fields = '__all__'

class PremioAdmin(RichTextFieldAdmin):
    form = PremioForm
    list_display = ('get_titulo_plain', 'año', 'get_desc_plain', 'bibliografía', 'foto', 'color_de_fondo')

admin.site.register(Premio_Nacional_de_Música, PremioAdmin)
# @admin.register(Premio_Nacional_de_Música)
# class PremioAdmin(RichTextFieldAdmin):
#     list_display = ('get_titulo_plain', 'año', 'get_desc_plain', 'bibliografía', 'foto', 'color_de_fondo')
#     list_filter = (YearFilter,)  # Agrega el filtro de año al admin


@admin.register(Acontecimiento)
class AcontecimientoAdmin(RichTextFieldAdmin):
    list_display = ('get_titulo_plain', 'fecha', 'get_desc_plain', 'enlace', 'color_de_fondo', 'foto')

# class MultimediasAdminForm(forms.ModelForm):
#     class Meta:
#         model = Multimedia
#         fields = '__all__'

#     def clean(self):
#         cleaned_data = super().clean()
#         archivo = cleaned_data.get('archivo')
#         foto = cleaned_data.get('foto')

#         if archivo or foto:
#             raise ValidationError('Un director no puede ser marcado como CEO y CTO al mismo tiempo.')

#         return cleaned_data

@admin.register(Multimedia)
class MultimediaAdmin(RichTextFieldAdmin):
    # form = MultimediasAdminForm
    list_display = ('get_titulo_plain', 'get_desc_plain', 'tipo', 'enlace', 'foto', 'color_de_fondo')

@admin.register(Efemerides)
class EfemeridesAdmin(RichTextFieldAdmin):
    list_display = ('get_titulo_plain', 'fecha', 'get_desc_plain', 'color_de_fondo', 'foto')

@admin.register(Redes)
class RedesAdmin(RichTextFieldAdmin):
    list_display = ('get_titulo_plain', 'enlace', 'foto')