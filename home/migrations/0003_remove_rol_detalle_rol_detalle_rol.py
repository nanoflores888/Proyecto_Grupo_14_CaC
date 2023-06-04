# Generated by Django 4.2 on 2023-05-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_persona_persona_rol_rol_alter_contacto_apellido_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rol',
            name='detalle',
        ),
        migrations.AddField(
            model_name='rol',
            name='detalle_rol',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'Aprobador'), (3, 'Autor')], default=3, verbose_name='DETALLE_ROL'),
        ),
    ]
