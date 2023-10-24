from django.contrib import admin
from apps.comentario.models import Comentario


# Register your models here.
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("publicacion", "autor", "contenido", "fecha_creacion")
