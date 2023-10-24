from django.db import models
from apps.inquilino.models import Inquilino
from apps.publicacion.models import Publicacion
from django.contrib.auth.models import User
from datetime import date


def get_fecha_actual():
    return date.today()


class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_creacion = models.DateField(default=get_fecha_actual)

    def __str__(self):
        return f"Comentario por {self.autor.username} en {self.publicacion.titulo}"
