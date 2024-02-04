from django.contrib import admin
from .models import Efemerides, Acontecimiento, Evento, Centros_y_Empresas, Directores, Historia_de_la_Institución, Multimedia, Premio_Nacional_de_Música


# Register your models here.
admin.site.register(Efemerides)
admin.site.register(Acontecimiento)
admin.site.register(Evento)
admin.site.register(Centros_y_Empresas)
admin.site.register(Directores)
admin.site.register(Historia_de_la_Institución)
admin.site.register(Multimedia)
admin.site.register(Premio_Nacional_de_Música)