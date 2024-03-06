from django.urls import path

from . import views

urlpatterns = [
    path('seccion/banner', views.get_banner_principal, name='get_banner_principal'),
    path('logos', views.get_iconos, name='get_iconos'),
    path('seccion/seccion-efemerides', views.get_seccion_efemerides, name='get_seccion_efemerides'),
    path('efemerides/', views.get_all_efem, name='efemerides'),
    path('efemerides/premio/', views.get_efem_premio, name='efemerides_premio'),
    path('acontecimiento/relevante/', views.get_acontecimiento_relevante, name='acontecimiento_relevante'),
    path('acontecimiento/banner/', views.get_acontecimiento_a_mostrar, name='acontecimiento_banner'),
    path('historia/', views.get_historia, name='historia'),
    path('centros-y-directores/', views.get_centros_y_directores, name='centros_y_directores'),
    path('premios/', views.get_premios, name='premios'),
    path('acontecimientos/semana/', views.get_acontecimientos_semana, name='acontecimientos_semana'),
    path('eventos/semana/', views.get_eventos_semana, name='eventos_semana'),
    path('acontecimientos/mes/', views.get_acontecimientos_mes, name='acontecimientos_mes'),
    path('eventos/mes/', views.get_eventos_mes, name='eventos_mes'),
    path('centros/contactos/', views.get_centros_contactos, name='centros_contactos'),
    path('directores/nombres/', views.get_directores_nombres, name='directores_nombres'),
]
