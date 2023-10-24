from django.urls import path
from django.contrib.auth.views import PasswordChangeView, LogoutView
from apps.comentario.views import EliminarComentarioView
from apps.publicacion.views import ViewPublicacionesView, DetallePublicacionView
from apps.inquilino import views

urlpatterns = [
    path(
        "registro_inquilino/", views.RegistroView.as_view(), name="registro_inquilino"
    ),
    path("login_inquilino/", views.LoginView.as_view(), name="login_inquilino"),
    path("perfil_inquilino/", views.PerfilView.as_view(), name="perfil_inquilino"),
    path(
        "editar_perfil_inquilino/",
        views.EditarPerfilView.as_view(),
        name="editar_inquilino",
    ),
    path("publicaciones/", ViewPublicacionesView.as_view(), name="publicaciones_view"),
    path(
        "detalle_publicacion/<int:pk>/",
        DetallePublicacionView.as_view(),
        name="detalle_publicacion",
    ),
    path(
        "eliminar_perfil/",
        views.EliminarPerfilView.as_view(),
        name="eliminar_inquilino",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path(
        "cambiar_contraseña/", PasswordChangeView.as_view(), name="cambiar_contraseña"
    ),
]
