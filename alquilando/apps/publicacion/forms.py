from django import forms
from apps.publicacion.models import Publicacion


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = [
            "titulo",
            "descripcion",
            "precio",
            "ubicacion",
            "estado",
            "fecha_publicacion",
        ]
