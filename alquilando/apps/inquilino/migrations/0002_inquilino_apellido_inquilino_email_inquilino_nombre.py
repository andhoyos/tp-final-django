# Generated by Django 4.2.5 on 2023-09-16 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquilino', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquilino',
            name='apellido',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inquilino',
            name='email',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inquilino',
            name='nombre',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
