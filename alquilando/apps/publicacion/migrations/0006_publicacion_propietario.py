# Generated by Django 4.2.5 on 2023-09-24 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propietario', '0005_propietario_password_alter_propietario_email'),
        ('publicacion', '0005_remove_publicacion_ubicacion_publicacion_barrio'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='propietario',
            field=models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to='propietario.propietario'),
            preserve_default=False,
        ),
    ]
