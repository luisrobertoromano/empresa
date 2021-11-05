from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Departamento)
admin.site.register(Habilidad)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'departamento',
        'job',
        'id',
    )

    search_fields = ('last_name', 'first_name')
    list_filter = ('job','habilidad','departamento')
    filter_horizontal = ('habilidad',)


admin.site.register(Empleado, EmpleadoAdmin)
