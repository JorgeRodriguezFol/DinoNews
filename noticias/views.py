from django.shortcuts import render
from .models import Noticia


def inicio(request):
    """
    Vista para la página de inicio del portal.
    
    Muestra información general sobre DinoNews.
    No requiere context porque es contenido estático.
    """
    return render(request, 'noticias/inicio.html')


def formulario(request):
    """
    Formulario para que usuarios propongan nuevas noticias.
    
    GET: Muestra el formulario vacío
    POST: En producción aquí se guardarían los datos
    
    Nota: Actualmente es solo un formulario HTML sin procesamiento
    para mantener la aplicación simple.
    """
    return render(request, 'noticias/formulario.html')


def noticias(request):
    """
    Lista todas las noticias ordenadas por fecha descendente.
    
    Context:
        - noticias: QuerySet con todas las Noticia, ordenadas por fecha
    
    Las noticias se traen directamente de la BD y se pasan al template
    para que las itere y las muestre de forma dinámica.
    """
    # Obtener todas las noticias (se ordenan automáticamente por el modelo)
    noticias_list = Noticia.objects.all()
    
    context = {
        'noticias': noticias_list
    }
    
    return render(request, 'noticias/noticias.html', context)
