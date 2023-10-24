# Generated by Django 4.2.5 on 2023-09-25 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquilino', '0007_inquilino_last_login_alter_inquilino_apellido_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquilino',
            name='last_login',
        ),
        migrations.AlterField(
            model_name='inquilino',
            name='apellido',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inquilino',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inquilino',
            name='nombre',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inquilino',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]