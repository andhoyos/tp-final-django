# Generated by Django 4.2.5 on 2023-09-25 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquilino', '0005_inquilino_password_alter_inquilino_apellido_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquilino',
            name='username',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
