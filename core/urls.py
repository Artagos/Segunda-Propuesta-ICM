# core/urls.py

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


# URLs que no dependen del idioma
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('infoweb321/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# URLs que dependen del idioma
localized_urlpatterns = [
    path('api/entidades/', include('apps.entidades.urls')),
]

urlpatterns += i18n_patterns(
    *localized_urlpatterns,
    prefix_default_language=True  # Cambia esto según tu necesidad
)

urlpatterns += [
    path('', TemplateView.as_view(template_name='index.html')),
]