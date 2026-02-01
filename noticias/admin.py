from django.contrib import admin
from .models import Noticia


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    """
    Configuración personalizada del panel de administración para Noticias.
    
    Proporciona interfaz para:
    - Ver lista de noticias con vista previa
    - Buscar por título o contenido
    - Filtrar por fecha de publicación
    - Crear, editar y eliminar noticias
    """
    
    # Columnas mostradas en la lista de noticias
    list_display = ('titulo', 'fecha_publicacion', 'preview_texto')
    
    # Campos donde se puede buscar
    # Se busca en titulo y en el contenido (texto)
    search_fields = ('titulo', 'texto')
    
    # Filtros disponibles en el sidebar derecho
    list_filter = ('fecha_publicacion',)
    
    # Ordenamiento por defecto (noticias más recientes primero)
    ordering = ('-fecha_publicacion',)
    
    # Organización de los campos en el formulario de edición
    fieldsets = (
        ('Información de la Noticia', {
            'fields': ('titulo', 'fecha_publicacion'),
            'description': 'Ingresa el título y selecciona la fecha de publicación'
        }),
        ('Contenido', {
            'fields': ('texto',),
            'description': 'Escribe el contenido completo de la noticia'
        }),
    )
    
    def preview_texto(self, obj):
        """
        Muestra una vista previa del contenido en la lista.
        
        Limita a 100 caracteres para que no ocupe demasiado espacio
        en la tabla de administración.
        """
        if len(obj.texto) > 100:
            return obj.texto[:100] + '...'
        return obj.texto
    
    preview_texto.short_description = 'Vista previa del contenido'
