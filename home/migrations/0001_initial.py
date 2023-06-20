# Generated by Django 4.2 on 2023-06-19 20:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='NOMBRE')),
                ('apellido', models.CharField(max_length=50, verbose_name='APELLIDO')),
                ('telefono', models.IntegerField(max_length=50, verbose_name='TELEFONO')),
                ('email', models.EmailField(max_length=254, verbose_name='EMAIL')),
                ('mensaje', models.CharField(max_length=1000, validators=[django.core.validators.MinLengthValidator(20)], verbose_name='MENSAJE')),
            ],
            options={
                'db_table': 'CONTACTO',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='NOMBRE')),
                ('apellido', models.CharField(max_length=100, verbose_name='APELLIDO')),
                ('email', models.EmailField(max_length=254, verbose_name='EMAIL')),
                ('contraseña', models.CharField(max_length=128, verbose_name='CONTRASEÑA')),
                ('estado_activo', models.BooleanField(default=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='USUARIO')),
            ],
            options={
                'db_table': 'PERSONA',
            },
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='TITULO')),
                ('contenido', models.TextField(max_length=5000, verbose_name='CONTENIDO')),
                ('estado', models.CharField(choices=[(1, 'Pendiente'), (2, 'Aprobada')], default=1, max_length=20, verbose_name='ESTADO')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='FECHA_CREACION')),
                ('fecha_modificacion', models.DateField(auto_now=True, null=True, verbose_name='FECHA_MODIFICACION')),
            ],
            options={
                'db_table': 'PUBLICACION',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle_rol', models.IntegerField(choices=[(1, 'Admin'), (2, 'Aprobador'), (3, 'Autor')], default=3, verbose_name='DETALLE_ROL')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='FECHA_CREACION')),
                ('fecha_modificacion', models.DateField(auto_now=True, null=True, verbose_name='FECHA_MODIFICACION')),
            ],
            options={
                'db_table': 'ROL',
            },
        ),
        migrations.CreateModel(
            name='Persona_rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='FECHA_CREACION')),
                ('fecha_modificacion', models.DateField(auto_now=True, null=True, verbose_name='FECHA_MODIFICACION')),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.persona', verbose_name='ID_PERSONA')),
                ('id_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.rol', verbose_name='ID_ROL')),
            ],
            options={
                'db_table': 'PERSONA_ROL',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField(max_length=500, verbose_name='CONTENIDO')),
                ('fecha_creacion', models.DateTimeField(auto_now=True, verbose_name='FECHA_CREACION')),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True, verbose_name='FECHA_MODIFICACION')),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.persona', verbose_name='ID_PERSONA')),
                ('id_publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.publicacion', verbose_name='ID_PUBLICACION')),
            ],
            options={
                'db_table': 'COMENTARIO',
            },
        ),
    ]
