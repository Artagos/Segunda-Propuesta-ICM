from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
import os

class CustomStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        name = os.path.normpath(name)  # Normaliza la ruta del archivo
        if self.exists(name):
            return name
        return super().get_available_name(name, max_length)

    def _save(self, name, content):
        # Normaliza y ajusta la ruta para reemplazar '\\' por '/'
        name = os.path.normpath(name).replace('\\', '/')
        if self.exists(name):
            return name
        return super()._save(name, content)

    def path(self, name):
        # Asegura que la ruta devuelta usa '/'
        return super().path(name).replace('\\', '/')
