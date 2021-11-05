from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'registro_app'

urlpatterns = [
    path(
        'listar-todo/', 
        views.EmpleadoListViewAll.as_view(), 
        name='listar-todo'
    ),
    path(
        'listar-por-area/<short_name>/', 
        views.EmpleadoListViewPorArea.as_view(), 
        name='listar-por-area'
    ),
    path(
        'buscar-por-apellido/', 
        views.EmpleadoListViewBuscar.as_view(), 
        name='buscar'
    ),
    path(
        'detalle/<pk>/', 
        views.EmpleadoDetailView.as_view(), 
        name='detalle'
    ),
    path(
        'exito/', 
        views.SuccessView.as_view(), 
        name='exito'
    ),
    path(
        'alta/', 
        views.EmpleadoCreateView.as_view(), 
        name='alta'
    ),
    path(
        'update/<pk>/', 
        views.EmpleadoUpdateView.as_view(), 
        name='update'
    ),
    path(
        'delete/<pk>/', 
        views.EmpleadoDeleteView.as_view(), 
        name='delete'
    ),
    path(
        '', 
        views.VistaPrincipal.as_view(), 
        name='index'
    ),
    
]