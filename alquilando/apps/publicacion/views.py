from django.shortcuts import render, redirect
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from apps.comentario.models import Comentario
from apps.publicacion.forms import PublicacionForm
from apps.publicacion.models import Publicacion
from apps.propietario.models import Propietario
from apps.inquilino.models import Inquilino
from django.contrib import messages
from django.urls import reverse_lazy


class ListarPublicacionesView(TemplateView):
    template_name = "publicacionesList.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # Si el usuario es un propietario, muestra sus publicaciones
            try:
                propietario = Propietario.objects.get(user=request.user)
                publicaciones = Publicacion.objects.filter(propietario=propietario)
                tiene_publicaciones = publicaciones.exists()
            except Propietario.DoesNotExist:
                messages.info(
                    request,
                    "No eres un propietario registrado. Por favor regístrate como propietario.",
                )
                return redirect(reverse_lazy("registro_propietario"))
        else:
            publicaciones = None
            tiene_publicaciones = False

        return render(
            request,
            self.template_name,
            {
                "publicaciones": publicaciones,
                "tiene_publicaciones": tiene_publicaciones,
            },
        )


class ViewPublicacionesView(TemplateView):
    template_name = "vista_publicaciones.html"

    def get(self, request, *args, **kwargs):
        orden = request.GET.get("ordenar_por", None)
        if request.user.is_authenticated:
            # Si el usuario es un inquilino, muestra todas las publicaciones
            try:
                inquilino = Inquilino.objects.get(user=request.user)
                if orden == "fecha":
                    publicaciones = Publicacion.objects.all().order_by(
                        "fecha_publicacion"
                    )
                elif orden == "precio":
                    publicaciones = Publicacion.objects.all().order_by("precio")
                else:
                    publicaciones = Publicacion.objects.all()

                tiene_publicaciones = publicaciones.exists()
            except Inquilino.DoesNotExist:
                messages.info(
                    request,
                    "No eres un inquilino registrado. Por favor regístrate para ver las publicaciones.",
                )
                return redirect(reverse_lazy("registro_inquilino"))
        else:
            publicaciones = None
            tiene_publicaciones = False

        return render(
            request,
            self.template_name,
            {
                "publicaciones": publicaciones,
                "tiene_publicaciones": tiene_publicaciones,
            },
        )


class DetallePublicacionView(DetailView):
    model = Publicacion
    template_name = "detalle_publicacion.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publicacion = self.get_object()
        comentarios = Comentario.objects.filter(publicacion=publicacion)
        context["comentarios"] = comentarios

        return context


class CrearPublicacionView(TemplateView):
    template_name = "publicacionesAdd.html"

    def get(self, request, *args, **kwargs):
        try:
            Propietario.objects.get(user=request.user)
        except Propietario.DoesNotExist:
            return redirect(reverse_lazy("registro_propietario"))

        form = PublicacionForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = PublicacionForm(request.POST)
        if form.is_valid():
            # Asocia la publicación al propietario
            try:
                propietario = Propietario.objects.get(user=request.user)
                publicacion = form.save(commit=False)
                publicacion.propietario = propietario
                publicacion.save()
                return redirect("listar_publicaciones")
            except Propietario.DoesNotExist:
                return redirect("listar_publicaciones")

        return render(request, self.template_name, {"form": form})


class EditarPublicacionView(UpdateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = "publicacionesUpdate.html"
    success_url = reverse_lazy("listar_publicaciones")

    def get(self, request, *args, **kwargs):
        # verifica que el usuario es el propietario de la publicación
        publicacion = self.get_object()
        propietario = Propietario.objects.get(user=request.user)
        if publicacion.propietario == propietario:
            messages.success(self.request, "Los datos se actualizaron correctamente.")
            return super().get(request, *args, **kwargs)
        else:
            return redirect("listar_publicaciones")


class EliminarPublicacionView(DeleteView):
    model = Publicacion
    template_name = "publicacionesDelete.html"
    success_url = reverse_lazy("listar_publicaciones")

    def get(self, request, *args, **kwargs):
        # verifica que el usuario es el propietario de la publicación
        publicacion = self.get_object()
        propietario = Propietario.objects.get(user=request.user)
        if publicacion.propietario == propietario:
            return super().get(request, *args, **kwargs)
        else:
            return redirect("listar_publicaciones")
