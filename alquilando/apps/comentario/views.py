from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from apps.publicacion.models import Publicacion
from apps.inquilino.models import Inquilino
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from apps.comentario.forms import ComentarioForm
from apps.comentario.models import Comentario


class ComentarioTemplateView(TemplateView):
    template_name = "agregar_comentario.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get("pk")
        context["publicacion"] = get_object_or_404(Publicacion, pk=pk)
        context["form"] = ComentarioForm()
        return context

    def post(self, request, pk):
        form = ComentarioForm(request.POST)
        if form.is_valid():
            publicacion = get_object_or_404(Publicacion, pk=pk)
            comentario = form.save(commit=False)
            comentario.publicacion = publicacion
            comentario.autor = request.user
            comentario.save()
            return redirect("detalle_publicacion", pk=pk)

        return self.render_to_response({"form": form})


class EditarComentarioView(UpdateView):
    model = Comentario
    form_class = ComentarioForm
    template_name = "editar_comentario.html"

    def get_success_url(self):
        comentario = self.get_object()
        return reverse("detalle_publicacion", kwargs={"pk": comentario.publicacion.pk})

    def get(self, request, *args, **kwargs):
        comentario = self.get_object()
        if comentario.autor == request.user:
            return super().get(request, *args, **kwargs)
        else:
            messages.error(request, "No tiene permiso para editar este comentario.")
            return redirect("detalle_publicacion", pk=comentario.publicacion.pk)


class EliminarComentarioView(DeleteView):
    model = Comentario
    template_name = "eliminar_comentario.html"

    def get_success_url(self):
        comentario = self.get_object()
        return reverse("detalle_publicacion", kwargs={"pk": comentario.publicacion.pk})

    def get(self, request, *args, **kwargs):
        comentario = self.get_object()
        if comentario.autor == request.user:
            return super().get(request, *args, **kwargs)
        else:
            messages.error(request, "No tiene permiso para eliminar este comentario.")
            return redirect("detalle_publicacion", pk=comentario.publicacion.pk)


class VerComentariosPublicacionView(DetailView):
    model = Publicacion
    template_name = "ver_comentarios_publicacion.html"
    context_object_name = "publicacion"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comentarios = Comentario.objects.filter(publicacion=self.object)
        context["comentarios"] = comentarios
        return context
