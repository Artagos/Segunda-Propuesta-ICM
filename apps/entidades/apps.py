from django.apps import AppConfig


class EntidadesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.entidades'

    def ready(self):
        from . import signals
        # from . import translation
