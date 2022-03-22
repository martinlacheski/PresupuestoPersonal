from django.db import models
from datetime import datetime
from core.choices import choices

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre', unique=True)
    
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        db_table = 'api_categorias'
        ordering = ['nombre']


class Operaciones(models.Model):
    concepto = models.CharField(max_length=100, verbose_name='Nombre', unique=True)
    monto = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name='Monto')
    fecha = models.DateField(default=datetime.now())
    tipo = models.CharField(choices=choices, max_length=100)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Operación'
        verbose_name_plural = 'Operaciones'
        db_table = 'api_operaciones'
        ordering = ['concepto']
