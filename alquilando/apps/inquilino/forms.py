from django import forms
from apps.inquilino.models import Inquilino


class RegistroInquilinoForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Inquilino
        fields = ["username", "nombre", "apellido", "email", "password"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("El nombre de usuario es obligatorio.")
        return username


class LoginInquilinoForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class PerfilInquilinoForm(forms.ModelForm):
    class Meta:
        model = Inquilino
        fields = [
            "username",
            "nombre",
            "apellido",
            "email",
        ]
