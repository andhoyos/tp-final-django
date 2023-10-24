from django import forms
from apps.propietario.models import Propietario


class RegistroPropietarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Propietario
        fields = ["username", "nombre", "apellido", "email", "password"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("El nombre de usuario es obligatorio.")
        return username


class LoginPropietarioForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class PerfilPropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = [
            "username",
            "nombre",
            "apellido",
            "email",
        ]
