from django.contrib import admin
from .models import Efemerides, Acontecimiento, Evento, Centros_y_Empresas, Directores, Historia_de_la_Institución, Multimedia, Premio_Nacional_de_Música
from .models import BannerPrincipal, Iconos, Revista, Podcast #ContenedorConFondo, ContenedorConFondoSoloTitulo, ContenedorICM,
from django import forms
from django.utils.html import strip_tags
from .forms import BannerPrincipalForm1, BannerPrincipalForm2, OpcionesForm
from django.http import HttpResponseRedirect
from django.utils.html import format_html
from django.urls import reverse






@admin.register(Revista)
class RevistaAdmin(admin.ModelAdmin):
    list_display = ('get_titulo_plain', 'get_desc_plain')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('titulo',)

    def get_titulo_plain(self, obj):
        return strip_tags(obj.titulo)
    get_titulo_plain.short_description = 'titulo'

    def get_desc_plain(self, obj):
        return strip_tags(obj.descripcion)
    get_desc_plain.short_description = 'descripcion'



@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_display = ('get_titulo_plain', 'get_desc_plain', 'link_podcast')
    search_fields = ('titulo', 'descripcion')
    list_filter = ('titulo',)

    def get_titulo_plain(self, obj):
        return strip_tags(obj.titulo)
    get_titulo_plain.short_description = 'titulo'

    def get_desc_plain(self, obj):
        return strip_tags(obj.descripcion)
    get_desc_plain.short_description = 'descripcion'



# class BannerPrincipalForm(forms.ModelForm):

#     numero_unico = forms.IntegerField(label='Posición del Contenedor')

#     # class Meta:
#     #     model = BannerPrincipal
#     #     fields = '__all__'

#     # OPCIONES = [('1', 'Agregar información personalizada'), ('2', 'Agregar información de una efeméride, acontecimiento o evento')]
#     # opcion = forms.ChoiceField(choices=OPCIONES, widget=forms.RadioSelect)

#     class Meta:
#         model = BannerPrincipal
#         fields = '__all__'

#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     if self.data.get('opcion') == '1':
#     #         self.fields['seleccionar_efemeride'].required = False
#     #         self.fields['seleccionar_acontecimiento'].required = False
#     #         self.fields['seleccionar_evento'].required = False
#     #     elif self.data.get('opcion') == '2':
#     #         self.fields['titulo'].required = False
#     #         self.fields['encabezado'].required = False
#     #         self.fields['descripcion'].required = False
#     #         self.fields['foto'].required = False
#     #         self.fields['color_de_fondo'].required = False

#     def clean(self):
#         cleaned_data = super().clean()
#         numero_unico = cleaned_data.get('numero_unico')
#         tipo_contenedor = cleaned_data.get('tipo_contenedor')
#         seleccionar_efemeride = cleaned_data.get('seleccionar_efemeride')
#         seleccionar_acontecimiento = cleaned_data.get('seleccionar_acontecimiento')
#         seleccionar_evento = cleaned_data.get('seleccionar_evento')

#         # Verificar si más de un tipo de contenedor ha sido seleccionado
#         selected = [bool(seleccionar_efemeride), bool(seleccionar_acontecimiento), bool(seleccionar_evento)]
#         if selected.count(True) > 1:
#             raise forms.ValidationError("Solo puedes seleccionar un tipo de contenedor a la vez.")


#         # Validar si el tipo_contenedor es efemeride, acontecimiento o evento y verificar que se haya seleccionado el elemento correspondiente
#         if tipo_contenedor == 'Efemeride':
#             if not seleccionar_efemeride:
#                 self.add_error('seleccionar_efemeride', 'Debe seleccionar una efemeride')
#             # if not color_de_fondo:
#             #     self.add_error('color_de_fondo', 'Debe seleccionar un color de fondo')

#         elif tipo_contenedor == 'Acontecimiento':
#             if not seleccionar_acontecimiento:
#                 self.add_error('seleccionar_acontecimiento', 'Debe seleccionar un acontecimiento.')
#             # if not color_de_fondo:
#             #     self.add_error('color_de_fondo', 'Debe seleccionar un color de fondo')
#         elif tipo_contenedor == 'Evento':
#             if not seleccionar_evento:
#                 self.add_error('seleccionar_evento', 'Debe seleccionar un evento.')
#             # if not color_de_fondo:
#             #     self.add_error('color_de_fondo', 'Debe seleccionar un color de fondo')


#         if numero_unico is not None:
#             # Validar que el número único no esté repetido
#             query = BannerPrincipal.objects.filter(numero_unico=numero_unico)
#             if self.instance.id:
#                 query = query.exclude(id=self.instance.id)
#             if query.exists():
#                 self.add_error('numero_unico', 'Este número ya está en uso.')
#         return cleaned_data





# @admin.register(BannerPrincipal)
# class BannerPrincipalAdmin(admin.ModelAdmin):
#     list_display = ('titulo', 'descripcion', 'numero_unico')

#     def get_form(self, request, obj=None, **kwargs):
#         # Decidir qué formulario mostrar basado en un parámetro GET
#         opcion = request.GET.get('opcion', '1')  # Opción por defecto es '1'
#         if opcion == '1':
#             form_class = BannerPrincipalForm1


#             def get_form(self, request, obj=None, **kwargs):
#                 form_class = super().get_form(request, obj, **kwargs)
#                 form_class.base_fields['titulo'].required = False
#                 form_class.base_fields['encabezado'].required = False
#                 form_class.base_fields['descripcion'].required = False
#                 form_class.base_fields['foto'].required = False
#                 form_class.base_fields['color_de_fondo'].required = False
#         elif opcion == '2':
#             form_class = BannerPrincipalForm2


#             def get_form(self, request, obj=None, **kwargs):
#                 form_class = super().get_form(request, obj, **kwargs)
#                 form_class.base_fields['seleccionar_efemeride'].required = False
#                 form_class.base_fields['seleccionar_acontecimiento'].required = False
#                 form_class.base_fields['seleccionar_evento'].required = False
#         else:
#             form_class = BannerPrincipalForm1


#             def get_form(self, request, obj=None, **kwargs):
#                 form_class = super().get_form(request, obj, **kwargs)
#                 form_class.base_fields['titulo'].required = False
#                 form_class.base_fields['encabezado'].required = False
#                 form_class.base_fields['descripcion'].required = False
#                 form_class.base_fields['foto'].required = False
#                 form_class.base_fields['color_de_fondo'].required = False
#         kwargs['form'] = form_class
#         return super().get_form(request, obj, **kwargs)



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

# class BannerPrincipalAdmin(admin.ModelAdmin):

#     list_display = ('titulo', 'descripcion', 'numero_unico', 'add_buttons')

    # def add_buttons(self, obj):
    #     return format_html(
    #         '<a class="button" href="{}">Agregar Personalizado</a>&nbsp;'
    #         '<a class="button" href="{}">Agregar Efeméride</a>',
    #         reverse('infoweb321:entidades_bannerprincipal_add') + '?opcion=1',
    #         reverse('infoweb321:entidades_bannerprincipal_add') + '?opcion=2'
    #     )
    # add_buttons.short_description = 'Agregar Banner'

    # def add_view(self, request, form_url='', extra_context=None):
    #     if 'opcion' not in request.GET:
    #         # Aquí podrías redirigir a una vista de selección o definir una opción por defecto
    #         return HttpResponseRedirect(reverse('infoweb321:entidades_bannerprincipal_add') + '?opcion=1')
        # return super().add_view(request, form_url, extra_context)

    # def get_form(self, request, obj=None, **kwargs):
    #     opcion = request.GET.get('opcion', '1')  # Asume opción 1 como predeterminada si no se proporciona
    #     if opcion == '1':
    #         form_class = BannerPrincipalForm1
    #     elif opcion == '2':
    #         form_class = BannerPrincipalForm2
    #     else:
    #         form_class = BannerPrincipalForm1  # Vuelve al formulario por defecto si 'opcion' no es válida

    #     kwargs['form'] = form_class
    #     return super().get_form(request, obj, **kwargs)

# class BannerPrincipalAdmin(admin.ModelAdmin):


    # def get_form(self, request, obj=None, **kwargs):
    #     # Asignar un formulario basado en el parámetro 'opcion' o usar un formulario base si 'opcion' no está disponible
    #     opcion = request.GET.get('opcion', '1')  # Asume opción 1 como predeterminada si no se proporciona
    #     if opcion == '1':
    #         form_class = BannerPrincipalForm1
    #     elif opcion == '2':
    #         form_class = BannerPrincipalForm2
    #     else:
    #         form_class = BannerPrincipalForm1  # Vuelve al formulario por defecto si 'opcion' no es válida

    #     kwargs['form'] = form_class
    #     return super().get_form(request, obj, **kwargs)

    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     # Agrega el parámetro 'opcion' al contexto para poder utilizarlo en la plantilla si es necesario
    #     extra_context = extra_context or {}
    #     if 'opcion' in request.GET:
    #         extra_context['opcion'] = request.GET['opcion']
    #     return super().change_view(request, object_id, form_url, extra_context)

# admin.site.register(BannerPrincipal, BannerPrincipalAdmin)


# class BannerPrincipalAdmin(admin.ModelAdmin):

#     form = BannerPrincipalForm

#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         # Establece los campos como no requeridos
#         form.base_fields['seleccionar_efemeride'].required = False
#         form.base_fields['seleccionar_acontecimiento'].required = False
#         form.base_fields['seleccionar_evento'].required = False
#         form.base_fields['titulo'].required = False
#         form.base_fields['encabezado'].required = False
#         form.base_fields['descripcion'].required = False
#         form.base_fields['foto'].required = False
#         form.base_fields['color_de_fondo'].required = False
#         # form.base_fields['color_de_letra'].required = False
#         # form.base_fields['color_boton'].required = False
#         # form.base_fields['color_letra_boton'].required = False
#         # form.base_fields['tipografia_titulo'].required = False
#         # form.base_fields['tipografia_encabezado'].required = False
#         # form.base_fields['tipografia_descripcion'].required = False
#         # form.base_fields['tipografia_enlace'].required = False
#         return form

#     pass

# class SeccionEfemerideForm(forms.ModelForm):

#     numero_unico = forms.IntegerField(label='Posición del Contenedor')

#     class Meta:
#         model = BannerPrincipal
#         fields = '__all__'

#     def clean(self):
#         cleaned_data = super().clean()
#         numero_unico = cleaned_data.get('numero_unico')

#         if numero_unico is not None:
#             # Validar que el número único no esté repetido
#             if BannerPrincipal.objects.filter(numero_unico=numero_unico).exists():
#                 self.add_error('numero_unico', 'Este número ya está en uso.')
#         return cleaned_data

# class SeccionEfemerideAdmin(admin.ModelAdmin):

#     form = SeccionEfemerideForm
#     pass




class RichTextFieldAdmin(admin.ModelAdmin):
    def get_titulo_plain(self, obj):
        return strip_tags(obj.titulo)
    get_titulo_plain.short_description = 'titulo'

    def get_desc_plain(self, obj):
        return strip_tags(obj.descripcion)
    get_desc_plain.short_description = 'descripcion'

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

@admin.register(Directores)
class DirectoresAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cargo', 'télefono', 'correo', 'consejo_de_dirección', 'empresa', 'foto')

@admin.register(Premio_Nacional_de_Música)
class PremioAdmin(RichTextFieldAdmin):
    list_display = ('get_titulo_plain', 'año', 'get_desc_plain', 'bibliografía', 'foto', 'color_de_fondo')

@admin.register(Acontecimiento)
class AcontecimientoAdmin(RichTextFieldAdmin):
    list_display = ('get_titulo_plain', 'fecha', 'get_desc_plain', 'enlace', 'color_de_fondo', 'foto')

@admin.register(Multimedia)
class MultimediaAdmin(RichTextFieldAdmin):
    list_display = ('get_titulo_plain', 'get_desc_plain', 'tipo', 'enlace', 'foto', 'color_de_fondo')

@admin.register(Efemerides)
class EfemeridesAdmin(RichTextFieldAdmin):
    list_display = ('get_titulo_plain', 'fecha', 'get_desc_plain', 'color_de_fondo', 'foto')