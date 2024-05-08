# # your_app_name/translation.py

# from modeltranslation.translator import register, TranslationOptions
# from .models import Podcast, Revista, Evento, Premio_Nacional_de_Música, Acontecimiento, Historia_de_la_Institución, Centros_y_Empresas, Directores, Multimedia, Efemerides, Redes, BannerPrincipal

# @register(Podcast)
# class PodcastTranslationOptions(TranslationOptions):
#     fields = ('titulo', 'descripcion',)

# @register(Revista)
# class RevistaTranslationOptions(TranslationOptions):
#     fields = ('titulo', 'descripcion',)

# @register(Evento)
# class EventoTranslationOptions(TranslationOptions):
#     fields = ('titulo', 'encabezado', 'descripcion','fecha')

# @register(Premio_Nacional_de_Música)
# class PremioNacionalDeMusicaTranslationOptions(TranslationOptions):
#     fields = ('titulo', 'descripcion', 'bibliografía',)

# @register(Acontecimiento)
# class AcontecimientoTranslationOptions(TranslationOptions):
#     fields = ('titulo', 'encabezado', 'descripcion','fecha')

# @register(Historia_de_la_Institución)
# class HistoriaDeLaInstitucionTranslationOptions(TranslationOptions):
#     fields = ('titulo', 'descripcion',)

# @register(Centros_y_Empresas)
# class CentrosYEmpresasTranslationOptions(TranslationOptions):
#     fields = ('nombre','dirección')

# @register(Directores)
# class DirectoresTranslationOptions(TranslationOptions):
#     fields = ('nombre','cargo')

# @register(Multimedia)
# class MultimediaTranslationOptions(TranslationOptions):
#     fields = ('titulo', 'descripcion',)

# @register(Efemerides)
# class EfemeridesTranslationOptions(TranslationOptions):
#     fields = ('titulo', 'encabezado', 'descripcion', 'fecha')

# @register(Redes)
# class RedesTranslationOptions(TranslationOptions):
#     fields = ('titulo',)

# @register(BannerPrincipal)
# class BannerPrincipalTranslationOptions(TranslationOptions):
#     fields = ('titulo', 'encabezado', 'descripcion')
