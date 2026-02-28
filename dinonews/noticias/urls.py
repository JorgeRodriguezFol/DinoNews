from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('formulario/', views.formulario, name='formulario'),
    path('noticias/', views.listado_noticias, name='noticias'),
]
