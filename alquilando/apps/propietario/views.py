from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from apps.propietario.forms import (
    RegistroPropietarioForm,
    LoginPropietarioForm,
    PerfilPropietarioForm,
)
from apps.propietario.models import Propietario
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    template_name = "index_propietario.html"


class RegistroView(TemplateView):
    template_name = "registro_propietario.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RegistroPropietarioForm()
        return context

    def post(self, request, *args, **kwargs):
        form = RegistroPropietarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            # Verifica si el usuario ya existe
            if User.objects.filter(username=username).exists():
                messages.error(request, "El nombre de usuario ya está en uso.")
                return redirect(reverse_lazy("registro_propietario"))
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )

            user.first_name = form.cleaned_data["nombre"]
            user.last_name = form.cleaned_data["apellido"]
            user.email = form.cleaned_data["email"]
            user.save()

            # Crear un objeto propietario asociado al usuario
            Propietario.objects.create(
                user=user,
                username=user.username,
                nombre=form.cleaned_data["nombre"],
                apellido=form.cleaned_data["apellido"],
                email=form.cleaned_data["email"],
            )

            messages.success(request, "Usuario registrado exitosamente.")
            return redirect("login_propietario")
        return render(request, self.template_name, {"form": form})


class LoginView(TemplateView):
    template_name = "login_propietario.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = LoginPropietarioForm()
        return context

    def post(self, request, *args, **kwargs):
        form = LoginPropietarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("listar_publicaciones")
            else:
                messages.error(request, "Los datos ingresados no son correctos.")
                return redirect("login_propietario")
        return render(request, self.template_name, {"form": form})


class EditarPerfilView(UpdateView):
    model = Propietario
    form_class = PerfilPropietarioForm
    template_name = "editar_perfil.html"
    success_url = reverse_lazy("perfil_propietario")

    def form_valid(self, form):
        messages.success(self.request, "Los datos se actualizaron correctamente.")
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user.propietario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar Perfil"
        return context


class PerfilView(TemplateView):
    template_name = "perfil_propietario.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                propietario = Propietario.objects.get(user=request.user)
                context = {"propietario": propietario}
            except Propietario.DoesNotExist:
                return redirect("registro_propietario")

            return render(request, self.template_name, context)
        else:
            return redirect("login_propietario")


class EliminarPerfilView(DeleteView):
    model = Propietario
    template_name = "eliminar_propietario.html"
    success_url = reverse_lazy("registro_propietario")

    def get_object(self, queryset=None):
        return self.request.user.propietario

    def get_success_url(self):
        return reverse_lazy("registro_propietario")
