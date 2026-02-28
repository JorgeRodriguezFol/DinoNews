from django.db import models

class Noticia(models.Model):
    """Modelo que representa una noticia sobre dinosaurios."""
    titulo = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    texto = models.TextField()

    def __str__(self):
        # muestra un título representativo en el admin
        return f"{self.titulo} ({self.fecha_publicacion})"
