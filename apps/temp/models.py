from django.db import models
from django.utils.translation import gettext_lazy as _


class Evento (models.Model):
    título = models.CharField(max_length=100)
    descripción = models.CharField(max_length=500)
    fecha = models.DateField()
    hora = models.TimeField()
    enlace = models.URLField(max_length=200)
    foto = models.FileField(_(""), upload_to='images/', max_length=100)
    mostrar_en_banner_principal = models.BooleanField()
    
    
    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]
    
    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]
    
    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    tipografía_de_título = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_título = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff')
    foto_de_fondo = models.FileField(_(""), upload_to='images/', max_length=100)
    
    
    def __str__(self):
        return self.título
    

class Historia_de_la_Institución (models.Model):
    class Meta:
        verbose_name_plural = "Historia_de_la_Institución"
    título = models.CharField(max_length=100)
    descripción = models.CharField(max_length=500)
    foto = models.FileField(_(""), upload_to='images/', max_length=100)
    tipografía = models.CharField(max_length=100)
    
    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]
    
    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]
    
    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    tipografía_de_título = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_título = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff')
    foto_de_fondo = models.FileField(_(""), upload_to='images/', max_length=100)
    
   
   
    def __str__(self):
        return self.título

class Centros_y_Empresas (models.Model):
    class Meta:
        verbose_name_plural = "Centros_y_Empresas"
    nombre = models.CharField(max_length=100)
    dirección = models.CharField(max_length=500)
    télefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100)
    
    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]
    
    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]
    
    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    tipografía_de_título = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_título = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff')
    foto_de_fondo = models.FileField(_(""), upload_to='images/', max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Directores (models.Model):
    class Meta:
        verbose_name_plural = "Directores"
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    télefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=100)
    consejo_de_dirección = models.BooleanField()
    empresa = models.OneToOneField("Centros_y_Empresas", on_delete=models.CASCADE)
    
    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]
    
    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]
    
    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
   
    
    def __str__(self):
        return self.nombre
    
class Premio_Nacional_de_Música (models.Model):
    class Meta:
        verbose_name_plural = "Premio_Nacional_de_Música"
    año = models.DateField()
    descripión = models.CharField(max_length=500)
    bibliografía = models.CharField(max_length=500)
    foto = models.FileField(_(""), upload_to='images/', max_length=100)
    
    
    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]
    
    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]
    
    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    # tipografía_de_título = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    # color_de_título = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff')
    foto_de_fondo = models.FileField(_(""), upload_to='images/', max_length=100)
   
    def __str__(self):
        return self.año

class Acontecimiento (models.Model):
    título = models.CharField(max_length=100)
    descripción = models.CharField(max_length=500)
    fecha_de_publicación = models.DateField()
    enlace = models.URLField(max_length=200)
    foto = models.FileField(_(""), upload_to='images/', max_length=100)
    mostrar_en_banner_principal = models.BooleanField()
    relevante = models.BooleanField()
    
    
    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]
    
    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]
    
    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    tipografía_de_título = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_título = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff')
    foto_de_fondo = models.FileField(_(""), upload_to='images/', max_length=100)
    
     
    def __str__(self):
        return self.título
    

class Multimedia (models.Model):
    nombre = models.CharField(max_length=100)
    descripción = models.CharField(max_length=500)
    tipo = models.CharField(max_length=100)
    enlace = models.URLField(max_length=200)
    foto = models.FileField(_(""), upload_to='images/', max_length=100)
    
    
    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]
    
    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]
    
    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    tipografía_de_título = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_título = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff')
    foto_de_fondo = models.FileField(_(""), upload_to='images/', max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Efemerides (models.Model):
    class Meta:
        verbose_name_plural = "Efemérides"
    fecha = models.DateField()
    descripción = models.CharField(max_length=500)
    foto = models.FileField(_(""), upload_to='images/', max_length=100)
    premio_nacional_de_la_música = models.OneToOneField("Premio_Nacional_de_Música", on_delete=models.CASCADE)
    enlace = models.URLField(max_length=200)
    mostrar_en_banner_principal = models.BooleanField()
    # relevante = models.BooleanField()
    
    
    TEXT_COLOR_CHOICES = [
        ('#000000', 'negro'),
        ('#ffffff','blanco'),
        ('#4f4f4f', 'gris'),
        ('#29385c', 'azul'),
        ('36454d', 'verde'),
        ('0d032b', 'malva'),
        ('ed8500', 'naranja'),
    ]
    
    TEXT_TIPOGRAPHY_CHOICES = [
        ('Bw Darius DEMO Bold', 'Bw Darius DEMO Bold'),
        ('Bw Darius DEMO Regular','Bw Darius DEMO Regular'),
        ('Montserrat Medium', 'Montserrat Medium'),
        ('Montserrat Regular','Montserrat Regular'),
        ('Montserrat Italic', 'Montserrat Italic'),
    ]
    
    tipografía_de_letra = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Montserrat Medium')
    tipografía_de_título = models.CharField(max_length=100, choices=TEXT_TIPOGRAPHY_CHOICES, default = 'Bw Darius DEMO Bold')
    color_de_letra = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_título = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#000000')
    color_de_fondo = models.CharField(max_length=7,choices=TEXT_COLOR_CHOICES, default='#ffffff')
    foto_de_fondo = models.FileField(_(""), upload_to='images/', max_length=100)