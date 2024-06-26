from django.urls import path

from . import views

from .views import select_banner_form

app_name = 'entidades'

urlpatterns = [
    path('revistas/', views.lista_revistas, name='lista_revistas'),
    path('revistas/<int:id>/', views.detalle_revista, name='detalle_revista'),
    path('podcasts/', views.lista_podcasts, name='lista_podcasts'),
    path('banner_principal/', views.get_banner_principal, name='get_banner_principal'),
    path('iconos/', views.get_iconos, name='get_iconos'),
    path('efemerides/', views.get_all_efem, name='get_all_efem'),
    path('efemerides/<int:day>/<int:month>/', views.get_efem_by_date, name='get_efem_by_date'),
    path('efemerides/<int:month>/', views.get_efem_by_month, name='get_efem_by_month'),
    path('acontecimientos/<int:month>/<int:year>/', views.get_acontecimiento_by_date, name='get_acontecimiento_by_date'),
    path('eventos/<int:month>/<int:year>/', views.get_evento_by_date, name='get_evento_by_date'),
    path('historia/', views.get_historia, name='get_historia'),
    path('directores/', views.get_centros_y_directores, name='get_centros_y_directores'),
    path('premios/', views.get_premios, name='get_premios'),
    path('acontecimientos_semana/', views.get_acontecimientos_semana, name='get_acontecimientos_semana'),
    path('eventos_semana/', views.get_eventos_semana, name='get_eventos_semana'),
    path('contactos/', views.get_centros_contactos, name='get_centros_contactos'),
    path('multimedias/', views.get_multimedias, name='get_multimedias'),
    path('multimedias/<int:id>/', views.detalle_multimedia, name='detalle_multimedia'),
    path("redes/", views.get_redes, name="get_redes"),
    path("get_cto/", views.get_cto, name="get_cto"),
    path("get_ceo/", views.get_ceo, name="get_ceo"),
    path('select-banner-form/', select_banner_form, name='bannerprincipal_select'),


]
