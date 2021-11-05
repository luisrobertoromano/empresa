from applications import registro
from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=50)

    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Habilidad(models.Model):
    """Model definition for Habilidad."""

    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        """Meta definition for Habilidad."""

        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        """Unicode representation of Habilidad."""
        return self.habilidad


class Empleado(models.Model):
    """Model definition for Empleado."""

    CARGO = (
        ('0','Jefe'),
        ('1','Administrativo'),
        ('2','Otro'),
    )

    first_name = models.CharField('Nombre', max_length=50)
    last_name = models.CharField('Apellido', max_length=50)
    full_name = models.CharField('Nombre completo', max_length=150, blank=True)
    job = models.CharField('Cargo', max_length=50, choices=CARGO)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidad = models.ManyToManyField(Habilidad)
    avatar = models.ImageField('Imagen', upload_to='registro', height_field=None, width_field=None, max_length=None, blank=True)


    class Meta:
        """Meta definition for Empleado."""

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        """Unicode representation of Empleado."""
        return self.last_name + ', ' + self.first_name
