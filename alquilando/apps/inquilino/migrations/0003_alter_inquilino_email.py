# Generated by Django 4.2.5 on 2023-09-16 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquilino', '0002_inquilino_apellido_inquilino_email_inquilino_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquilino',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
