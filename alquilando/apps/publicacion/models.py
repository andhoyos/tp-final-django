from django.db import models
from datetime import date
from apps.propietario.models import Propietario


def get_fecha_actual():
    return date.today()


# Create your models here.
class Publicacion(models.Model):
    TITULO_MAX_LENGTH = 100
    DESCRIPCION_MAX_LENGTH = 500
    UBICACION_MAX_LENGTH = 200

    ESTADO_CHOICES = [
        ("disponible", "Disponible"),
        ("reservado", "Reservado"),
        ("alquilado", "Alquilado"),
    ]

    titulo = models.CharField(max_length=TITULO_MAX_LENGTH)
    descripcion = models.CharField(max_length=DESCRIPCION_MAX_LENGTH)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    ubicacion = models.CharField(max_length=UBICACION_MAX_LENGTH)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField(default=get_fecha_actual)

    def __str__(self):
        return self.titulo
