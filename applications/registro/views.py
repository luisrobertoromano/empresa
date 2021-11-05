from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from django.urls import reverse_lazy
from .models import Empleado
from .forms import EmpleadoForm

# Create your views here.


class EmpleadoListViewAll(ListView):
    model = Empleado
    template_name = "registro/list_all.html"
    ordering = 'last_name'
    context_object_name = 'lista'
    paginate_by = 4

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            last_name__icontains = palabra_clave
        )
        return lista


class EmpleadoListViewPorArea(ListView):
    model = Empleado
    template_name = "registro/list_por_area.html"
    context_object_name = 'lista'

    def get_queryset(self):
        area = self.kwargs['short_name']
        lista = Empleado.objects.filter(
            departamento__short_name = area
        )
        return lista


class EmpleadoListViewBuscar(ListView):
    model = Empleado
    template_name = "registro/buscar.html"
    context_object_name = 'lista'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
            last_name = palabra_clave
        )
        return lista


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "registro/detalle.html"
    context_object_name = 'detalle'


class SuccessView(TemplateView):
    template_name = "registro/exito.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "registro/alta.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('registro_app:listar-todo')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "registro/update.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('registro_app:listar-todo')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "registro/delete.html"
    success_url = reverse_lazy('registro_app:listar-todo')


class VistaPrincipal(TemplateView):
    template_name = "index.html"



