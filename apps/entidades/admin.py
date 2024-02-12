from django.contrib import admin
from .models import Efemerides, Acontecimiento, Evento, Centros_y_Empresas, Directores, Historia_de_la_Institución, Multimedia, Premio_Nacional_de_Música
from .models import BannerPrincipal, Seccion_Efemerides, ContenedorConFondo, ContenedorConFondoSoloTitulo, ContenedorICM
from django import forms

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
        
        # Validar si el tipo_contenedor es efemeride, acontecimiento o evento y verificar que se haya seleccionado el elemento correspondiente
        if tipo_contenedor == 'Efemeride':
            if not seleccionar_efemeride:
                self.add_error('seleccionar_efemeride', 'Debe seleccionar una efemeride')
        elif tipo_contenedor == 'Acontecimiento':
            if not seleccionar_acontecimiento:
                self.add_error('seleccionar_acontecimiento', 'Debe seleccionar un acontecimiento.')
        elif tipo_contenedor == 'Evento':
            if not seleccionar_evento:
                self.add_error('seleccionar_evento', 'Debe seleccionar un evento.')
        
        if numero_unico is not None:
            # Validar que el número único no esté repetido
            if BannerPrincipal.objects.filter(numero_unico=numero_unico).exists():
                self.add_error('numero_unico', 'Este número ya está en uso.')
        return cleaned_data
    # class Meta:
    #     model = BannerPrincipal
    #     fields = '__all__'

    # def clean(self):
        # form = super().clean()
        # # seleccionar_efemeride = form.get("seleccionar_efemeride")
        # # seleccionar_acontecimiento = form.get("seleccionar_acontecimiento")
        # # seleccionar_evento = form.get("seleccionar_evento")

        # # # Verifica si se han seleccionado más de dos opciones
        # # if (
        # #     seleccionar_efemeride and 
        # #     (seleccionar_acontecimiento or seleccionar_evento)
        # # ) or (
        # #     seleccionar_acontecimiento and 
        # #     (seleccionar_efemeride or seleccionar_evento)
        # # ) or (
        # #     seleccionar_evento and 
        # #     (seleccionar_efemeride or seleccionar_acontecimiento)
        # # ):
        # #     raise forms.ValidationError("Solo se puede seleccionar una opción entre Efemeride, Acontecimiento y Evento")
        # form.base_fields['seleccionar_efemeride'].required = False
        # form.base_fields['seleccionar_acontecimiento'].required = False
        # form.base_fields['seleccionar_evento'].required = False
        # form.base_fields['titulo'].required = False
        # form.base_fields['encabezado'].required = False
        # form.base_fields['descripcion'].required = False
        # form.base_fields['enlace'].required = False
        # form.base_fields['foto'].required = False
        # form.base_fields['color_de_fondo'].required = False
        # form.base_fields['color_de_letra'].required = False
        # form.base_fields['color_boton'].required = False
        # form.base_fields['color_letra_boton'].required = False
        # form.base_fields['tipografia_titulo'].required = False
        # form.base_fields['tipografia_encabezado'].required = False
        # form.base_fields['tipografia_descripcion'].required = False
        # form.base_fields['tipografia_enlace'].required = False
        
        # return form

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
        form.base_fields['enlace'].required = False
        form.base_fields['foto'].required = False
        form.base_fields['color_de_fondo'].required = False
        form.base_fields['color_de_letra'].required = False
        form.base_fields['color_boton'].required = False
        form.base_fields['color_letra_boton'].required = False
        form.base_fields['tipografia_titulo'].required = False
        form.base_fields['tipografia_encabezado'].required = False
        form.base_fields['tipografia_descripcion'].required = False
        form.base_fields['tipografia_enlace'].required = False
        return form

    pass
    
class SeccionEfemerideForm(forms.ModelForm):
    
    numero_unico = forms.IntegerField(label='Posición del Contenedor')

    class Meta:
        model = BannerPrincipal
        fields = '__all__'
        
    def clean(self):
        cleaned_data = super().clean()
        numero_unico = cleaned_data.get('numero_unico')
        
        if numero_unico is not None:
            # Validar que el número único no esté repetido
            if BannerPrincipal.objects.filter(numero_unico=numero_unico).exists():
                self.add_error('numero_unico', 'Este número ya está en uso.')
        return cleaned_data  
    
class SeccionEfemerideAdmin(admin.ModelAdmin):
    
    form = SeccionEfemerideForm
    pass

admin.site.register(BannerPrincipal, BannerPrincipalAdmin)
admin.site.register(Seccion_Efemerides, SeccionEfemerideAdmin)

# Register your models here.
admin.site.register(Efemerides)
admin.site.register(Acontecimiento)
admin.site.register(Evento)
admin.site.register(Centros_y_Empresas)
admin.site.register(Directores)
admin.site.register(Historia_de_la_Institución)
admin.site.register(Multimedia)
admin.site.register(Premio_Nacional_de_Música)
