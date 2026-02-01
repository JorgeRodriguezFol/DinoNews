from django.urls import path
from . import views

# Definición de las URLs de la app noticias
urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio en /
    path('formulario/', views.formulario, name='formulario'),  # Formulario en /formulario/
    path('noticias/', views.noticias, name='noticias'),  # Listado de noticias en /noticias/
]
