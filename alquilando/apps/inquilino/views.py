from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from apps.inquilino.forms import (
    PerfilInquilinoForm,
    RegistroInquilinoForm,
    LoginInquilinoForm,
)
from apps.inquilino.models import Inquilino
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RegistroView(TemplateView):
    template_name = "registro_inquilino.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RegistroInquilinoForm()
        return context

    def post(self, request, *args, **kwargs):
        form = RegistroInquilinoForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            if User.objects.filter(username=username).exists():
                messages.error(request, "El nombre de usuario ya está en uso.")
                return redirect("registro_inquilino")

            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )

            user.first_name = form.cleaned_data["nombre"]
            user.last_name = form.cleaned_data["apellido"]
            user.email = form.cleaned_data["email"]
            user.save()

            # Crear un objeto Inquilino asociado al usuario
            Inquilino.objects.create(
                user=user,
                username=user.username,
                nombre=form.cleaned_data["nombre"],
                apellido=form.cleaned_data["apellido"],
                email=form.cleaned_data["email"],
            )

            messages.success(request, "Usuario registrado exitosamente.")
            return redirect("login_inquilino")
        return render(request, self.template_name, {"form": form})


class LoginView(TemplateView):
    template_name = "login_inquilino.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LoginInquilinoForm()
        return context

    def post(self, request, *args, **kwargs):
        form = LoginInquilinoForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect("publicaciones_view")
            else:
                messages.error(request, "Los datos ingresados no son correctos.")

                return redirect("login_inquilino")
        return render(request, self.template_name, {"form": form})


class EditarPerfilView(UpdateView):
    model = Inquilino
    form_class = PerfilInquilinoForm
    template_name = "editar_inquilino.html"
    success_url = reverse_lazy("perfil_inquilino")

    def form_valid(self, form):
        messages.success(self.request, "Los datos se actualizaron correctamente.")
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user.inquilino

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar Perfil"
        return context


class PerfilView(TemplateView):
    template_name = "perfil_inquilino.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                inquilino = Inquilino.objects.get(user=request.user)
                context = {"inquilino": inquilino}
            except Inquilino.DoesNotExist:
                return redirect("registro_inquilino")

            return render(request, self.template_name, context)
        else:
            return redirect("login_inquilino")


class EliminarPerfilView(DeleteView):
    model = Inquilino
    template_name = "eliminar_inquilino.html"
    success_url = reverse_lazy("registro_inquilino")

    def get_object(self, queryset=None):
        return self.request.user.inquilino

    def get_success_url(self):
        return reverse_lazy("registro_inquilino")


class CambiarContraseñaView(PasswordChangeView):
    template_name = "cambiar_contraseña.html"
    success_url = reverse_lazy("detalle_perfil")
