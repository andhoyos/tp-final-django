# Generated by Django 4.2.5 on 2023-10-01 23:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('publicacion', '0011_alter_publicacion_fecha_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]