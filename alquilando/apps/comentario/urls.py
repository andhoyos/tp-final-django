from django.urls import path

from apps.comentario.views import (
    ComentarioTemplateView,
    EditarComentarioView,
    EliminarComentarioView,
    VerComentariosPublicacionView,
)

urlpatterns = [
    path(
        "agregar_comentario/<int:pk>/",
        ComentarioTemplateView.as_view(),
        name="agregar_comentario",
    ),
    path(
        "editar_comentario/<int:pk>/",
        EditarComentarioView.as_view(),
        name="editar_comentario",
    ),
    path(
        "eliminar_comentario/<int:pk>/",
        EliminarComentarioView.as_view(),
        name="eliminar_comentario",
    ),
    path(
        "ver_comentarios/<int:pk>/",
        VerComentariosPublicacionView.as_view(),
        name="ver_comentarios_publicacion",
    ),
]
