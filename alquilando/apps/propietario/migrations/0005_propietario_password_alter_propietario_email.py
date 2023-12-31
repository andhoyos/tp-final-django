# Generated by Django 4.2.5 on 2023-09-24 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propietario', '0004_propietario_apellido_propietario_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='propietario',
            name='password',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='propietario',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]
