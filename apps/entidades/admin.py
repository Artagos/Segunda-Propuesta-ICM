from django.contrib import admin
from .models import Efemerides, Acontecimiento, Evento, Centros_y_Empresas, Directores, Historia_de_la_Institución, Multimedia, Premio_Nacional_de_Música
from .models import BannerPrincipal, ContenedorConFondo, ContenedorConFondoSoloTitulo, ContenedorICM
from django import forms

# class BannerPrincipalAdmin(admin.ModelAdmin):
#     list_display = ('tipo_contenedor', 'contenido')
#     list_filter = ('tipo_contenedor',)
#     search_fields = ['tipo_contenedor']
#     readonly_fields = ['contenido']
#     fieldsets = (
#         (None, {
#             'fields': ('tipo_contenedor',)
#         }),
#         ('Contenido', {
#             'fields': ('contenido',),
#         }),
#     )
   
# class BannerPrincipalForm(forms.ModelForm):
#     class Meta:
#         model = BannerPrincipal
#         fields = ['tipo_contenedor',]  # Agrega los demás campos aquí
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['tipo_contenedor'].widget.attrs['onchange'] = 'banner_template()'
        
# class BannerPrincipalAdmin(admin.ModelAdmin):
#     form = BannerPrincipalForm

# class BannerPrincipalForm(forms.ModelForm):
#     class Meta:
#         model = BannerPrincipal
#         fields = '__all__'

# class BannerPrincipalAdmin(admin.ModelAdmin):
#     form = BannerPrincipalForm

#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         if obj:
#             form.base_fields['instancia_contenedor'].queryset = obj.obtener_instancias_disponibles()
#         return form

#     list_display = ('tipo_contenedor',)
#     search_fields = ('tipo_contenedor',)
# Register the Admin classes for Book using the decorator






# class BannerPrincipalAdmin(admin.ModelAdmin):
#     list_display = ('tipo_contenedor', 'contenido')

# class EfemeridesInstanceInLine(admin.TabularInline):
#     model = BannerPrincipal

# class EfemeridesAdmin(admin.ModelAdmin):
#     list_display = ('titulo', 'fecha', 'descripcion')
#     inlines = [EfemeridesInstanceInLine]


class BannerPrincipalAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Establece los campos como no requeridos
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
    
    

admin.site.register(BannerPrincipal, BannerPrincipalAdmin)

# Register your models here.
admin.site.register(Efemerides)
admin.site.register(Acontecimiento)
admin.site.register(Evento)
admin.site.register(Centros_y_Empresas)
admin.site.register(Directores)
admin.site.register(Historia_de_la_Institución)
admin.site.register(Multimedia)
admin.site.register(Premio_Nacional_de_Música)
