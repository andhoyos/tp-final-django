# Generated by Django 4.2.5 on 2023-09-25 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquilino', '0006_inquilino_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquilino',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='inquilino',
            name='apellido',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inquilino',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inquilino',
            name='nombre',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='inquilino',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
