from django.db import models
from django.utils import timezone

# Modelo que representa cada noticia en la base de datos
# Cada noticia tiene un título, fecha y contenido de texto
class Noticia(models.Model):
    """
    Almacena información de noticias sobre dinosaurios.
    
    Campos:
        - titulo: Encabezado de la noticia (máx 200 caracteres)
        - fecha_publicacion: Cuándo se publicó (por defecto hoy)
        - texto: Contenido completo de la noticia
    
    Notas:
        - Se ordena por fecha descendente (más recientes primero)
        - El plural en admin se configura en Meta
    """
    titulo = models.CharField(
        max_length=200, 
        help_text="Encabezado de la noticia"
    )
    fecha_publicacion = models.DateField(
        default=timezone.now,
        help_text="Fecha en que se publica la noticia"
    )
    texto = models.TextField(
        help_text="Contenido completo y detallado de la noticia"
    )
    
    class Meta:
        verbose_name_plural = "Noticias"
        ordering = ['-fecha_publicacion']
        indexes = [
            models.Index(fields=['-fecha_publicacion']),
        ]
    
    def __str__(self):
        return self.titulo
    
    def preview(self):
        """Retorna un resumen corto del contenido"""
        return self.texto[:150] + '...' if len(self.texto) > 150 else self.texto
