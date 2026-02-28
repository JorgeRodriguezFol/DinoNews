from django.shortcuts import render, redirect
from .models import Noticia

# Vista para la página de inicio

def inicio(request):
    return render(request, 'noticias/inicio.html')

# Vista para mostrar el formulario (no guarda nada)
def formulario(request):
    if request.method == 'POST':
        # aquí se podrían procesar los datos
        return redirect('inicio')
    return render(request, 'noticias/formulario.html')

# Vista para listar todas las noticias desde la base de datos
def listado_noticias(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'noticias/noticias.html', {'noticias': noticias})
