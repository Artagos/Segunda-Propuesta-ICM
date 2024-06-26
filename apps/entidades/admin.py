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
from modeltranslation.admin import TranslationAdmin
# from . import translation
from django.utils.translation import get_language




class RichTextFieldAdmin(admin.ModelAdmin):
    # def get_titulo_plain(self, obj):
    #     return strip_tags(obj.titulo)
    # get_titulo_plain.short_description = 'Título'

    def get_titulo_plain(self, obj):
        current_language = get_language()
        if current_language == 'en':
            titulo = obj.titulo_en
        elif current_language == 'es':
            titulo = obj.titulo_es
        # else:
        #     titulo = obj.titulo

        if titulo is None or titulo == '':
            return None
        else:
            return strip_tags(titulo)
    get_titulo_plain.short_description = 'Titulo'

    def get_bibliografía_plain(self, obj):
        current_language = get_language()
        if current_language == 'en':
            bibliografía = obj.bibliografía_en
        elif current_language == 'es':
            bibliografía = obj.bibliografía_es
        # else:
        #     titulo = obj.titulo

        if bibliografía is None or bibliografía == '':
            return None
        else:
            return strip_tags(bibliografía)
    get_bibliografía_plain.short_description = 'Bibliografía'

    def get_desc_plain(self, obj):
        current_language = get_language()
        if current_language == 'en':
            descripcion = obj.descripcion_en
        elif current_language == 'es':
            descripcion = obj.descripcion_es

        if descripcion is None or descripcion == '':
            return None
        else:
            return strip_tags(descripcion)


    get_desc_plain.short_description = 'Descripción'

    def get_enc_plain(self, obj):
        current_language = get_language()
        if current_language == 'en':
            encabezado = obj.encabezado_en
        elif current_language == 'es':
            encabezado = obj.encabezado_es

        if encabezado is None or encabezado == '':
            return None
        else:
            return strip_tags(encabezado)


    get_enc_plain.short_description = 'Encabezado'

    def get_name_plain(self, obj):
        current_language = get_language()
        if current_language == 'en':
            nombre = obj.nombre_en
        elif current_language == 'es':
            nombre = obj.nombre_es

        if nombre is None or nombre == '':
            return None
        else:
            return strip_tags(nombre)


    get_name_plain.short_description = 'Nombre'

    def get_cargo_plain(self, obj):
        current_language = get_language()
        if current_language == 'en':
            cargo = obj.cargo_en
        elif current_language == 'es':
            cargo = obj.cargo_es

        if cargo is None or cargo == '':
            return None
        else:
            return strip_tags(cargo)


    get_cargo_plain.short_description = 'Cargo'

    def get_dirección_plain(self, obj):
        current_language = get_language()
        if current_language == 'en':
            dirección = obj.dirección_en
        elif current_language == 'es':
            dirección = obj.dirección_es

        if dirección is None or dirección == '':
            return None
        else:
            return strip_tags(dirección)


    get_dirección_plain.short_description = 'Dirección'


class RevistaAdminForm(forms.ModelForm):
    class Meta:
        model = Revista
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(RevistaAdminForm, self).__init__(*args, **kwargs)
        # Hacer que los campos de idioma sean obligatorios
        # Obtener el idioma actual de la sesión
        current_language = get_language()

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        for field_name in self.fields:
            if field_name.endswith(f'_{current_language}'):
                self.fields[field_name].required = True
            else:
                self.fields[field_name].required = False
        # Cambiar las etiquetas
        self.fields['titulo_en'].label = 'Title'
        self.fields['titulo_es'].label = 'Título'
        # Cambiar las etiquetas
        self.fields['descripcion_en'].label = 'Description'
        self.fields['descripcion_es'].label = 'Descripcion'

    def clean_pdf(self):
        pdf = self.cleaned_data.get('pdf')
        if pdf:
            if not pdf.name.endswith('.pdf'):
                raise forms.ValidationError('El archivo debe ser un PDF.')
        return pdf



class EventoAdminForm(forms.ModelForm,TranslationAdmin):
    class Meta:
        model = Evento
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EventoAdminForm, self).__init__(*args, **kwargs)
        # Hacer que los campos de idioma sean obligatorios
        # Obtener el idioma actual de la sesión
        current_language = get_language()

        if (current_language == 'en'):
            not_current = 'es'
        else:
            not_current = 'en'

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        for field_name in self.fields:
            if field_name.endswith(f'_{current_language}'):
                self.fields[field_name].required = True
            elif field_name.endswith(f'_{not_current}'):
                self.fields[field_name].required = False
        # Cambiar las etiquetas
        self.fields['titulo_en'].label = 'Title'
        self.fields['titulo_es'].label = 'Título'
        # Cambiar las etiquetas
        self.fields['descripcion_en'].label = 'Description'
        self.fields['descripcion_es'].label = 'Descripcion'

        self.fields['encabezado_en'].label = 'Subtitle'
        self.fields['encabezado_es'].label = 'Encabezado'

        # self.fields['fecha_en'].label = 'Date'
        # self.fields['fecha_es'].label = 'Fecha'

class PremioNacionalDeMusicaAdminForm(forms.ModelForm):
    current_year = datetime.datetime.now().year
    year_choices = [(year, year) for year in range(1997, current_year + 1)]
    año = forms.ChoiceField(choices=year_choices)

    class Meta:
        model = Premio_Nacional_de_Música
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(PremioNacionalDeMusicaAdminForm, self).__init__(*args, **kwargs)
        # Hacer que los campos de idioma sean obligatorios
        # Obtener el idioma actual de la sesión
        current_language = get_language()

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        if (current_language == 'en'):
            not_current = 'es'
        else:
            not_current = 'en'

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        for field_name in self.fields:
            if field_name.endswith(f'_{current_language}'):
                self.fields[field_name].required = True
            elif field_name.endswith(f'_{not_current}'):
                self.fields[field_name].required = False
        # Cambiar las etiquetas
        self.fields['titulo_en'].label = 'Title'
        self.fields['titulo_es'].label = 'Título'
        # Cambiar las etiquetas
        self.fields['descripcion_en'].label = 'Description'
        self.fields['descripcion_es'].label = 'Descripcion'

        self.fields['bibliografía_en'].label = 'Bibliography'
        self.fields['bibliografía_es'].label = 'Bibliografía'



class AcontecimientoAdminForm(forms.ModelForm):
    class Meta:
        model = Acontecimiento
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(AcontecimientoAdminForm, self).__init__(*args, **kwargs)
        # Hacer que los campos de idioma sean obligatorios
        # Obtener el idioma actual de la sesión
        current_language = get_language()

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        if (current_language == 'en'):
            not_current = 'es'
        else:
            not_current = 'en'

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        for field_name in self.fields:
            if field_name.endswith(f'_{current_language}'):
                self.fields[field_name].required = True
            elif field_name.endswith(f'_{not_current}'):
                self.fields[field_name].required = False
        # Cambiar las etiquetas
        self.fields['titulo_en'].label = 'Title'
        self.fields['titulo_es'].label = 'Título'
        # Cambiar las etiquetas
        self.fields['descripcion_en'].label = 'Description'
        self.fields['descripcion_es'].label = 'Descripcion'

        self.fields['encabezado_en'].label = 'Subtitle'
        self.fields['encabezado_es'].label = 'Encabezado'

        # self.fields['fecha_en'].label = 'Date'
        # self.fields['fecha_es'].label = 'Fecha'

class HistoriaDeLaInstitucionAdminForm(forms.ModelForm):
    class Meta:
        model = Historia_de_la_Institución
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(HistoriaDeLaInstitucionAdminForm, self).__init__(*args, **kwargs)
        # Hacer que los campos de idioma sean obligatorios
        # Obtener el idioma actual de la sesión
        current_language = get_language()

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        if (current_language == 'en'):
            not_current = 'es'
        else:
            not_current = 'en'

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        for field_name in self.fields:
            if field_name.endswith(f'_{current_language}'):
                self.fields[field_name].required = True
            elif field_name.endswith(f'_{not_current}'):
                self.fields[field_name].required = False
        # Cambiar las etiquetas
        self.fields['titulo_en'].label = 'Title'
        self.fields['titulo_es'].label = 'Título'
        # Cambiar las etiquetas
        self.fields['descripcion_en'].label = 'Description'
        self.fields['descripcion_es'].label = 'Descripcion'


class CentrosYEmpresasAdminForm(forms.ModelForm):
    class Meta:
        model = Centros_y_Empresas
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CentrosYEmpresasAdminForm, self).__init__(*args, **kwargs)
        # Hacer que los campos de idioma sean obligatorios
        # Obtener el idioma actual de la sesión
        current_language = get_language()

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        if (current_language == 'en'):
            not_current = 'es'
        else:
            not_current = 'en'

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        for field_name in self.fields:
            if field_name.endswith(f'_{current_language}'):
                self.fields[field_name].required = True
            elif field_name.endswith(f'_{not_current}'):
                self.fields[field_name].required = False
        # Cambiar las etiquetas
        self.fields['nombre_en'].label = 'Name'
        self.fields['nombre_es'].label = 'Nombre'
        # Cambiar las etiquetas
        self.fields['dirección_en'].label = 'Address'
        self.fields['dirección_es'].label = 'Dirección'



class DirectoresAdminForm(forms.ModelForm):
    class Meta:
        model = Directores
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DirectoresAdminForm, self).__init__(*args, **kwargs)
        # Hacer que los campos de idioma sean obligatorios
        # Obtener el idioma actual de la sesión
        current_language = get_language()

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        if (current_language == 'en'):
            not_current = 'es'
        else:
            not_current = 'en'

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        for field_name in self.fields:
            if field_name.endswith(f'_{current_language}'):
                self.fields[field_name].required = True
            elif field_name.endswith(f'_{not_current}'):
                self.fields[field_name].required = False
        # Cambiar las etiquetas
        self.fields['nombre_en'].label = 'Name'
        self.fields['nombre_es'].label = 'Nombre'
        # Cambiar las etiquetas
        self.fields['cargo_en'].label = 'Work Position'
        self.fields['cargo_es'].label = 'Cargo'

    def clean(self):
        cleaned_data = super().clean()
        es_ceo = cleaned_data.get('es_ceo')
        es_cto = cleaned_data.get('es_cto')

        if es_ceo and es_cto:
            raise ValidationError('Un director no puede ser marcado como CEO y CTO al mismo tiempo.')

        return cleaned_data

class MultimediaAdminForm(forms.ModelForm):
    class Meta:
        model = Multimedia
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(MultimediaAdminForm, self).__init__(*args, **kwargs)
        # Hacer que los campos de idioma sean obligatorios
        # Obtener el idioma actual de la sesión
        current_language = get_language()

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        if (current_language == 'en'):
            not_current = 'es'
        else:
            not_current = 'en'

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        for field_name in self.fields:
            if field_name.endswith(f'_{current_language}'):
                self.fields[field_name].required = True
            elif field_name.endswith(f'_{not_current}'):
                self.fields[field_name].required = False
        # Cambiar las etiquetas
        self.fields['titulo_en'].label = 'Title'
        self.fields['titulo_es'].label = 'Título'
        # Cambiar las etiquetas
        self.fields['descripcion_en'].label = 'Description'
        self.fields['descripcion_es'].label = 'Descripcion'


class EfemeridesAdminForm(forms.ModelForm):
    class Meta:
        model = Efemerides
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(EfemeridesAdminForm, self).__init__(*args, **kwargs)
        # Hacer que los campos de idioma sean obligatorios
        # Obtener el idioma actual de la sesión
        current_language = get_language()

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        if (current_language == 'en'):
            not_current = 'es'
        else:
            not_current = 'en'

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        for field_name in self.fields:
            if field_name.endswith(f'_{current_language}'):
                self.fields[field_name].required = True
            elif field_name.endswith(f'_{not_current}'):
                self.fields[field_name].required = False
        # Cambiar las etiquetas
        self.fields['titulo_en'].label = 'Title'
        self.fields['titulo_es'].label = 'Título'
        # Cambiar las etiquetas
        self.fields['descripcion_en'].label = 'Description'
        self.fields['descripcion_es'].label = 'Descripcion'

        self.fields['encabezado_en'].label = 'Subtitle'
        self.fields['encabezado_es'].label = 'Encabezado'

        # self.fields['fecha_en'].label = 'Date'
        # self.fields['fecha_es'].label = 'Fecha'

class RedesAdminForm(forms.ModelForm):
    class Meta:
        model = Redes
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(RedesAdminForm, self).__init__(*args, **kwargs)
        # Hacer que los campos de idioma sean obligatorios
        # Obtener el idioma actual de la sesión
        current_language = get_language()

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        if (current_language == 'en'):
            not_current = 'es'
        else:
            not_current = 'en'

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        for field_name in self.fields:
            if field_name.endswith(f'_{current_language}'):
                self.fields[field_name].required = True
            elif field_name.endswith(f'_{not_current}'):
                self.fields[field_name].required = False
        # Cambiar las etiquetas
        self.fields['titulo_en'].label = 'Title'
        self.fields['titulo_es'].label = 'Título'



class BannerPrincipalAdminForm(forms.ModelForm):
    class Meta:
        model = BannerPrincipal
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(BannerPrincipalAdminForm, self).__init__(*args, **kwargs)
        # Hacer que los campos de idioma sean obligatorios
        # Obtener el idioma actual de la sesión
        current_language = get_language()

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        if (current_language == 'en'):
            not_current = 'es'
        else:
            not_current = 'en'

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        for field_name in self.fields:
            if field_name.endswith(f'_{current_language}'):
                self.fields[field_name].required = True
            elif field_name.endswith(f'_{not_current}'):
                self.fields[field_name].required = False

        # Cambiar las etiquetas
        self.fields['titulo_en'].label = 'Title'
        self.fields['titulo_es'].label = 'Título'
        # Cambiar las etiquetas
        self.fields['descripcion_en'].label = 'Description'
        self.fields['descripcion_es'].label = 'Descripcion'

        self.fields['encabezado_en'].label = 'Subtitle'
        self.fields['encabezado_es'].label = 'Encabezado'




@admin.register(Revista)
class RevistaAdmin(RichTextFieldAdmin):
    form = RevistaAdminForm

    list_display = ('get_titulo_plain', 'get_desc_plain', 'fecha','pdf', 'imagen_portada')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        current_language = get_language()
        if current_language == 'en':
            return qs.exclude(titulo_en__isnull=True).exclude(titulo_en='')
        elif current_language == 'es':
            return qs.exclude(titulo_es__isnull=True).exclude(titulo_es='')
        else:
            return qs.exclude(titulo__isnull=True).exclude(titulo='')
    def get_form(self, request, obj=None, **kwargs):
        # Llamar a la implementación base para obtener el formulario inicial
        form = super().get_form(request, obj, **kwargs)

        # Obtener el idioma actualmente activo
        current_language = get_language()

        # Ciclar a través de todos los campos del formulario
        for field_name in list(form.base_fields):
            if field_name.endswith('_en') or field_name.endswith('_es'):
                # Habilitar solo los campos del idioma actual
                if not field_name.endswith(f'_{current_language}'):
                    form.base_fields[field_name].widget = forms.HiddenInput()

        return form

class PodcastAdminForm(forms.ModelForm):
    class Meta:
        model = Podcast
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PodcastAdminForm, self).__init__(*args, **kwargs)
        # Hacer que los campos de idioma sean obligatorios
        # Obtener el idioma actual de la sesión
        current_language = get_language()

        # Ajustar los campos de idioma para ser obligatorios solo si están en el idioma actual
        for field_name in self.fields:
            if field_name.endswith(f'_{current_language}'):
                self.fields[field_name].required = True
            else:
                self.fields[field_name].required = False
        # Cambiar las etiquetas
        self.fields['titulo_en'].label = 'Title'
        self.fields['titulo_es'].label = 'Título'
        # Cambiar las etiquetas
        self.fields['descripcion_en'].label = 'Description'
        self.fields['descripcion_es'].label = 'Descripcion'

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
    list_display = ('get_titulo_plain', 'get_desc_plain', 'link_podcast', 'archivo_local', 'foto')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        current_language = get_language()
        if current_language == 'en':
            return qs.exclude(titulo_en__isnull=True).exclude(titulo_en='')
        elif current_language == 'es':
            return qs.exclude(titulo_es__isnull=True).exclude(titulo_es='')
        else:
            return qs.exclude(titulo__isnull=True).exclude(titulo='')

    def get_form(self, request, obj=None, **kwargs):
        # Llamar a la implementación base para obtener el formulario inicial
        form = super().get_form(request, obj, **kwargs)

        # Obtener el idioma actualmente activo
        current_language = get_language()

        # Ciclar a través de todos los campos del formulario
        for field_name in list(form.base_fields):
            if field_name.endswith('_en') or field_name.endswith('_es'):
                # Habilitar solo los campos del idioma actual
                if not field_name.endswith(f'_{current_language}'):
                    form.base_fields[field_name].widget = forms.HiddenInput()

        return form


@admin.register(BannerPrincipal)
class BannerPrincipalAdmin(RichTextFieldAdmin):
    Form = BannerPrincipalAdminForm
    list_display = ('get_titulo_plain', 'get_enc_plain', 'get_desc_plain', 'foto', 'color_de_fondo', 'numero_unico', 'seleccionar_efemeride', 'seleccionar_acontecimiento', 'seleccionar_evento')
    # def get_list_display(self, request):
    #     default_fields = [field.name for field in self.model._meta.fields if field.name != 'id']
    #     return ['get_titulo_plain'] + default_fields


    def get_queryset(self, request):
        qs = super().get_queryset(request)
        current_language = get_language()
        if current_language == 'en':
            return qs.exclude(titulo_en__isnull=True).exclude(titulo_en='')
        elif current_language == 'es':
            return qs.exclude(titulo_es__isnull=True).exclude(titulo_es='')
        else:
            return qs.exclude(titulo__isnull=True).exclude(titulo='')

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

        current_language = get_language()



        # Configura las opciones de tipo_contenedor según la opción seleccionada
        Form.base_fields['tipo_contenedor'].choices = tipo_contenedor_choices

        # Establece los campos como no requeridos basados en la opción
        if opcion == '2':
            for field_name in ['seleccionar_efemeride', 'seleccionar_acontecimiento', 'seleccionar_evento']:
                Form.base_fields[field_name].required = False
        elif opcion == '1':
            # for field_name in ['titulo', 'encabezado', 'descripcion', 'foto', 'color_de_fondo']:
            #     Form.base_fields[field_name].required = False

            for field_name in list(Form.base_fields):
                if field_name.endswith('_en') or field_name.endswith('_es'):
                    # Habilitar solo los campos del idioma actual
                    if not field_name.endswith(f'_{current_language}'):
                        Form.base_fields[field_name].widget = forms.HiddenInput()

#  # Obtener el idioma actualmente activo
#         current_language = get_language()

#         # Ciclar a través de todos los campos del formulario
        # for field_name in list(Form.base_fields):
        #     if field_name.endswith('_en') or field_name.endswith('_es'):
        #         # Habilitar solo los campos del idioma actual
        #         if not field_name.endswith(f'_{current_language}'):
        #             Form.base_fields[field_name].widget = forms.HiddenInput()






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
    form = EventoAdminForm
    list_display = ('get_titulo_plain', 'fecha', 'get_desc_plain', 'enlace', 'hora', 'color_de_fondo', 'foto')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        current_language = get_language()
        if current_language == 'en':
            return qs.exclude(titulo_en__isnull=True).exclude(titulo_en='')
        elif current_language == 'es':
            return qs.exclude(titulo_es__isnull=True).exclude(titulo_es='')
        # else:
        #     return qs.exclude(titulo__isnull=True).exclude(titulo='')

    def get_form(self, request, obj=None, **kwargs):
        # Llamar a la implementación base para obtener el formulario inicial
        form = super().get_form(request, obj, **kwargs)

        # Obtener el idioma actualmente activo
        current_language = get_language()

        # Ciclar a través de todos los campos del formulario
        for field_name in list(form.base_fields):
            if field_name.endswith('_en') or field_name.endswith('_es'):
                # Habilitar solo los campos del idioma actual
                if not field_name.endswith(f'_{current_language}'):
                    form.base_fields[field_name].widget = forms.HiddenInput()

        return form

@admin.register(Historia_de_la_Institución)
class HistoriaAdmin(RichTextFieldAdmin):
    form = HistoriaDeLaInstitucionAdminForm
    list_display = ('get_titulo_plain', 'get_desc_plain', 'foto', 'color_de_fondo')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        current_language = get_language()
        if current_language == 'en':
            return qs.exclude(titulo_en__isnull=True).exclude(titulo_en='')
        elif current_language == 'es':
            return qs.exclude(titulo_es__isnull=True).exclude(titulo_es='')
        else:
            return qs.exclude(titulo__isnull=True).exclude(titulo='')

    def get_form(self, request, obj=None, **kwargs):
        # Llamar a la implementación base para obtener el formulario inicial
        form = super().get_form(request, obj, **kwargs)

        # Obtener el idioma actualmente activo
        current_language = get_language()

        # Ciclar a través de todos los campos del formulario
        for field_name in list(form.base_fields):
            if field_name.endswith('_en') or field_name.endswith('_es'):
                # Habilitar solo los campos del idioma actual
                if not field_name.endswith(f'_{current_language}'):
                    form.base_fields[field_name].widget = forms.HiddenInput()

        return form

@admin.register(Centros_y_Empresas)
class CentrosAdmin(RichTextFieldAdmin):
    form = CentrosYEmpresasAdminForm
    list_display = ('get_name_plain', 'get_dirección_plain', 'télefono', 'correo')

    def get_form(self, request, obj=None, **kwargs):
        # Llamar a la implementación base para obtener el formulario inicial
        form = super().get_form(request, obj, **kwargs)

        # Obtener el idioma actualmente activo
        current_language = get_language()

        # Ciclar a través de todos los campos del formulario
        for field_name in list(form.base_fields):
            if field_name.endswith('_en') or field_name.endswith('_es'):
                # Habilitar solo los campos del idioma actual
                if not field_name.endswith(f'_{current_language}'):
                    form.base_fields[field_name].widget = forms.HiddenInput()

        return form

# class DirectoresAdminForm(forms.ModelForm):
#     class Meta:
#         model = Directores
#         fields = '__all__'

#     def clean(self):
#         cleaned_data = super().clean()
#         es_ceo = cleaned_data.get('es_ceo')
#         es_cto = cleaned_data.get('es_cto')

#         if es_ceo and es_cto:
#             raise ValidationError('Un director no puede ser marcado como CEO y CTO al mismo tiempo.')

#         return cleaned_data



@admin.register(Directores)
class DirectoresAdmin(RichTextFieldAdmin):
    form = DirectoresAdminForm
    list_display = ('get_name_plain', 'get_cargo_plain', 'télefono', 'correo', 'consejo_de_dirección', 'empresa', 'foto', 'es_ceo','es_cto')

    def get_form(self, request, obj=None, **kwargs):
        # Llamar a la implementación base para obtener el formulario inicial
        form = super().get_form(request, obj, **kwargs)

        # Obtener el idioma actualmente activo
        current_language = get_language()

        # Ciclar a través de todos los campos del formulario
        for field_name in list(form.base_fields):
            if field_name.endswith('_en') or field_name.endswith('_es'):
                # Habilitar solo los campos del idioma actual
                if not field_name.endswith(f'_{current_language}'):
                    form.base_fields[field_name].widget = forms.HiddenInput()

        return form


# class PremioForm(forms.ModelForm):
#     current_year = datetime.datetime.now().year
#     year_choices = [(year, year) for year in range(1997, current_year + 1)]
#     año = forms.ChoiceField(choices=year_choices)

#     class Meta:
#         model = Premio_Nacional_de_Música
#         fields = '__all__'
@admin.register(Premio_Nacional_de_Música)
class PremioAdmin(RichTextFieldAdmin):
    form = PremioNacionalDeMusicaAdminForm
    list_display = ('get_titulo_plain', 'año', 'get_desc_plain', 'get_bibliografía_plain', 'foto', 'color_de_fondo')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        current_language = get_language()
        if current_language == 'en':
            return qs.exclude(titulo_en__isnull=True).exclude(titulo_en='')
        elif current_language == 'es':
            return qs.exclude(titulo_es__isnull=True).exclude(titulo_es='')
        else:
            return qs.exclude(titulo__isnull=True).exclude(titulo='')

    def get_form(self, request, obj=None, **kwargs):
        # Llamar a la implementación base para obtener el formulario inicial
        form = super().get_form(request, obj, **kwargs)

        # Obtener el idioma actualmente activo
        current_language = get_language()

        # Ciclar a través de todos los campos del formulario
        for field_name in list(form.base_fields):
            if field_name.endswith('_en') or field_name.endswith('_es'):
                # Habilitar solo los campos del idioma actual
                if not field_name.endswith(f'_{current_language}'):
                    form.base_fields[field_name].widget = forms.HiddenInput()

        return form

# admin.site.register(Premio_Nacional_de_Música, PremioNacionalDeMusicaAdminForm)
# @admin.register(Premio_Nacional_de_Música)
# class PremioAdmin(RichTextFieldAdmin):
#     list_display = ('get_titulo_plain', 'año', 'get_desc_plain', 'bibliografía', 'foto', 'color_de_fondo')
#     list_filter = (YearFilter,)  # Agrega el filtro de año al admin


@admin.register(Acontecimiento)
class AcontecimientoAdmin(RichTextFieldAdmin):
    form=AcontecimientoAdminForm
    list_display = ('get_titulo_plain','get_enc_plain', 'fecha', 'get_desc_plain', 'enlace', 'color_de_fondo', 'foto')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        current_language = get_language()
        if current_language == 'en':
            return qs.exclude(titulo_en__isnull=True).exclude(titulo_en='')
        elif current_language == 'es':
            return qs.exclude(titulo_es__isnull=True).exclude(titulo_es='')
        else:
            return qs.exclude(titulo__isnull=True).exclude(titulo='')

    def get_form(self, request, obj=None, **kwargs):
        # Llamar a la implementación base para obtener el formulario inicial
        form = super().get_form(request, obj, **kwargs)

        # Obtener el idioma actualmente activo
        current_language = get_language()

        # Ciclar a través de todos los campos del formulario
        for field_name in list(form.base_fields):
            if field_name.endswith('_en') or field_name.endswith('_es'):
                # Habilitar solo los campos del idioma actual
                if not field_name.endswith(f'_{current_language}'):
                    form.base_fields[field_name].widget = forms.HiddenInput()

        return form

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
    form = MultimediaAdminForm
    list_display = ('get_titulo_plain', 'get_desc_plain', 'tipo', 'enlace', 'foto', 'color_de_fondo')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        current_language = get_language()
        if current_language == 'en':
            return qs.exclude(titulo_en__isnull=True).exclude(titulo_en='')
        elif current_language == 'es':
            return qs.exclude(titulo_es__isnull=True).exclude(titulo_es='')
        else:
            return qs.exclude(titulo__isnull=True).exclude(titulo='')

    def get_form(self, request, obj=None, **kwargs):
        # Llamar a la implementación base para obtener el formulario inicial
        form = super().get_form(request, obj, **kwargs)

        # Obtener el idioma actualmente activo
        current_language = get_language()

        # Ciclar a través de todos los campos del formulario
        for field_name in list(form.base_fields):
            if field_name.endswith('_en') or field_name.endswith('_es'):
                # Habilitar solo los campos del idioma actual
                if not field_name.endswith(f'_{current_language}'):
                    form.base_fields[field_name].widget = forms.HiddenInput()

        return form

@admin.register(Efemerides)
class EfemeridesAdmin(RichTextFieldAdmin):
    form = EfemeridesAdminForm
    list_display = ('get_titulo_plain', 'get_enc_plain','fecha', 'get_desc_plain', 'color_de_fondo', 'foto')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        current_language = get_language()
        if current_language == 'en':
            return qs.exclude(titulo_en__isnull=True).exclude(titulo_en='')
        elif current_language == 'es':
            return qs.exclude(titulo_es__isnull=True).exclude(titulo_es='')
        else:
            return qs.exclude(titulo__isnull=True).exclude(titulo='')

    def get_form(self, request, obj=None, **kwargs):
        # Llamar a la implementación base para obtener el formulario inicial
        form = super().get_form(request, obj, **kwargs)

        # Obtener el idioma actualmente activo
        current_language = get_language()

        # Ciclar a través de todos los campos del formulario
        for field_name in list(form.base_fields):
            if field_name.endswith('_en') or field_name.endswith('_es'):
                # Habilitar solo los campos del idioma actual
                if not field_name.endswith(f'_{current_language}'):
                    form.base_fields[field_name].widget = forms.HiddenInput()

        return form

@admin.register(Redes)
class RedesAdmin(RichTextFieldAdmin):
    form = RedesAdminForm
    list_display = ('get_titulo_plain', 'enlace', 'foto')
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        current_language = get_language()
        if current_language == 'en':
            return qs.exclude(titulo_en__isnull=True).exclude(titulo_en='')
        elif current_language == 'es':
            return qs.exclude(titulo_es__isnull=True).exclude(titulo_es='')
        else:
            return qs.exclude(titulo__isnull=True).exclude(titulo='')

    def get_form(self, request, obj=None, **kwargs):
        # Llamar a la implementación base para obtener el formulario inicial
        form = super().get_form(request, obj, **kwargs)

        # Obtener el idioma actualmente activo
        current_language = get_language()

        # Ciclar a través de todos los campos del formulario
        for field_name in list(form.base_fields):
            if field_name.endswith('_en') or field_name.endswith('_es'):
                # Habilitar solo los campos del idioma actual
                if not field_name.endswith(f'_{current_language}'):
                    form.base_fields[field_name].widget = forms.HiddenInput()

        return form