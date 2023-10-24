from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.inquilino.models import Inquilino


class InquilinoAdmin(UserAdmin):
    model = Inquilino
    list_display = ("username", "nombre", "apellido", "email", "is_staff")
    search_fields = ("username", "nombre", "apellido", "email")

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Inquilino, InquilinoAdmin)
