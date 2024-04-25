from django import forms
from .models import BannerPrincipal

class OpcionesForm(forms.Form):
    OPCIONES = [
        ('1', 'Agregar información personalizada'),
        ('2', 'Agregar información de una efeméride, acontecimiento o evento')
    ]
    opcion = forms.ChoiceField(choices=OPCIONES, widget=forms.RadioSelect)

class BannerPrincipalForm1(forms.ModelForm):


    class Meta:
        model = BannerPrincipal
        fields = ['tipo_contenedor','titulo', 'descripcion','encabezado' ,'color_de_fondo' ,'foto' ,'numero_unico']

    numero_unico = forms.IntegerField(label='Posición del Contenedor')



    def clean(self):
        cleaned_data = super().clean()
        numero_unico = cleaned_data.get('numero_unico')


        if numero_unico is not None:
            # Validar que el número único no esté repetido
            query = BannerPrincipal.objects.filter(numero_unico=numero_unico)
            if self.instance.id:
                query = query.exclude(id=self.instance.id)
            if query.exists():
                self.add_error('numero_unico', 'Este número ya está en uso.')
        return cleaned_data

class BannerPrincipalForm2(forms.ModelForm):



    class Meta:
        model = BannerPrincipal
        fields = ['tipo_contenedor','seleccionar_efemeride','seleccionar_acontecimiento','seleccionar_evento','numero_unico']

    numero_unico = forms.IntegerField(label='Posición del Contenedor')



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