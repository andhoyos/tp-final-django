from django.urls import path
from apps.publicacion.views import (
    CrearPublicacionView,
    EditarPublicacionView,
    EliminarPublicacionView,
)

urlpatterns = [
    path("crear/", CrearPublicacionView.as_view(), name="crear_publicacion"),
    path(
        "editar/<int:pk>/",
        EditarPublicacionView.as_view(),
        name="editar_publicacion",
    ),
    path(
        "eliminar/<int:pk>/",
        EliminarPublicacionView.as_view(),
        name="eliminar_publicacion",
    ),
]
