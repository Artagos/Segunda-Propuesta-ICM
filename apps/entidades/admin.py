from django.contrib import admin
from .models import Efemerides, Acontecimiento, Evento, Centros_y_Empresas, Directores, Historia_de_la_Institución, Multimedia, Premio_Nacional_de_Música
from .models import BannerPrincipal, Iconos, Revista, Podcast #ContenedorConFondo, ContenedorConFondoSoloTitulo, ContenedorICM,
from django import forms
from django.utils.html import strip_tags



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

class BannerPrincipalForm(forms.ModelForm):

    numero_unico = forms.IntegerField(label='Posición del Contenedor')

    class Meta:
        model = BannerPrincipal
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        numero_unico = cleaned_data.get('numero_unico')
        tipo_contenedor = cleaned_data.get('tipo_contenedor')
        seleccionar_efemeride = cleaned_data.get('seleccionar_efemeride')
        seleccionar_acontecimiento = cleaned_data.get('seleccionar_acontecimiento')
        seleccionar_evento = cleaned_data.get('seleccionar_evento')

        # Verificar si más de un tipo de contenedor ha sido seleccionado
        selected = [bool(seleccionar_efemeride), bool(seleccionar_acontecimiento), bool(seleccionar_evento)]
        if selected.count(True) > 1:
            raise forms.ValidationError("Solo puedes seleccionar un tipo de contenedor a la vez.")


        # Validar si el tipo_contenedor es efemeride, acontecimiento o evento y verificar que se haya seleccionado el elemento correspondiente
        if tipo_contenedor == 'Efemeride':
            if not seleccionar_efemeride:
                self.add_error('seleccionar_efemeride', 'Debe seleccionar una efemeride')
            # if not color_de_fondo:
            #     self.add_error('color_de_fondo', 'Debe seleccionar un color de fondo')

        elif tipo_contenedor == 'Acontecimiento':
            if not seleccionar_acontecimiento:
                self.add_error('seleccionar_acontecimiento', 'Debe seleccionar un acontecimiento.')
            # if not color_de_fondo:
            #     self.add_error('color_de_fondo', 'Debe seleccionar un color de fondo')
        elif tipo_contenedor == 'Evento':
            if not seleccionar_evento:
                self.add_error('seleccionar_evento', 'Debe seleccionar un evento.')
            # if not color_de_fondo:
            #     self.add_error('color_de_fondo', 'Debe seleccionar un color de fondo')


        if numero_unico is not None:
            # Validar que el número único no esté repetido
            query = BannerPrincipal.objects.filter(numero_unico=numero_unico)
            if self.instance.id:
                query = query.exclude(id=self.instance.id)
            if query.exists():
                self.add_error('numero_unico', 'Este número ya está en uso.')
        return cleaned_data

class BannerPrincipalAdmin(admin.ModelAdmin):

    form = BannerPrincipalForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Establece los campos como no requeridos
        form.base_fields['seleccionar_efemeride'].required = False
        form.base_fields['seleccionar_acontecimiento'].required = False
        form.base_fields['seleccionar_evento'].required = False
        form.base_fields['titulo'].required = False
        form.base_fields['encabezado'].required = False
        form.base_fields['descripcion'].required = False
        form.base_fields['foto'].required = False
        form.base_fields['color_de_fondo'].required = False
        # form.base_fields['color_de_letra'].required = False
        # form.base_fields['color_boton'].required = False
        # form.base_fields['color_letra_boton'].required = False
        # form.base_fields['tipografia_titulo'].required = False
        # form.base_fields['tipografia_encabezado'].required = False
        # form.base_fields['tipografia_descripcion'].required = False
        # form.base_fields['tipografia_enlace'].required = False
        return form

    pass

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



admin.site.register(BannerPrincipal, BannerPrincipalAdmin)

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