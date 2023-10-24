from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


class Inquilino(AbstractUser):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    # Relación con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    groups = models.ManyToManyField("auth.Group", related_name="inquilino_groups")
    user_permissions = models.ManyToManyField(
        "auth.Permission", related_name="inquilino_user_permissions"
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
