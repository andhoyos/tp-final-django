from django.urls import path
from apps.propietario import views
from django.contrib.auth import views as auth_views
from apps.publicacion.views import ListarPublicacionesView

urlpatterns = [
    path(
        "registro_propietario/",
        views.RegistroView.as_view(),
        name="registro_propietario",
    ),
    path("login_propietario/", views.LoginView.as_view(), name="login_propietario"),
    path("perfil_propietario/", views.PerfilView.as_view(), name="perfil_propietario"),
    path(
        "editar_perfil/",
        views.EditarPerfilView.as_view(),
        name="editar_perfil",
    ),
    path(
        "eliminar_perfil/",
        views.EliminarPerfilView.as_view(),
        name="eliminar_propietario",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path(
        "listar_publicaciones/",
        ListarPublicacionesView.as_view(),
        name="listar_publicaciones",
    ),
]
