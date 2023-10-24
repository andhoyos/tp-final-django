from django.contrib import admin
from apps.publicacion.models import Publicacion


class PublicacionAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "descripcion",
        "precio",
        "ubicacion",
        "estado",
        "fecha_publicacion",
    )
    list_filter = ("estado",)
    search_fields = ("titulo", "ubicacion")


admin.site.register(Publicacion, PublicacionAdmin)
