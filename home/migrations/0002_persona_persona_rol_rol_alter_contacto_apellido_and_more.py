# Generated by Django 4.2 on 2023-05-23 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='NOMBRE')),
                ('apellido', models.CharField(max_length=100, verbose_name='APELLIDO')),
                ('email', models.EmailField(max_length=254, verbose_name='ENAIL')),
                ('contraseña', models.CharField(max_length=128, verbose_name='CONTRASEÑA')),
                ('estado_activo', models.BooleanField(default=1)),
            ],
            options={
                'db_table': 'PERSONA',
            },
        ),
        migrations.CreateModel(
            name='Persona_rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='FECHA_CREACION')),
                ('fecha_modificacion', models.DateField(auto_now=True, null=True, verbose_name='FECHA_MODIFICACION')),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.persona', verbose_name='ID_ROL')),
            ],
            options={
                'db_table': 'PERSONA_ROL',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=50, verbose_name='DETALLE')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='FECHA_CREACION')),
                ('fecha_modificacion', models.DateField(auto_now=True, null=True, verbose_name='FECHA_MODIFICACION')),
            ],
            options={
                'db_table': 'ROL',
            },
        ),
        migrations.AlterField(
            model_name='contacto',
            name='apellido',
            field=models.CharField(max_length=30, verbose_name='APELLIDO'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='EMAIL'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='mensaje',
            field=models.CharField(max_length=600, verbose_name='MENSAJE'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='NOMBRE'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='telefono',
            field=models.IntegerField(verbose_name='TELEFONO'),
        ),
        migrations.AlterModelTable(
            name='contacto',
            table='CONTACTO',
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='TITULO')),
                ('contenido', models.TextField(max_length=5000, verbose_name='CONTENIDO')),
                ('estado', models.CharField(max_length=20, verbose_name='ESTADO')),
                ('fecha_creacion', models.DateField(auto_now=True, verbose_name='FECHA_CREACION')),
                ('fecha_modificacion', models.DateField(auto_now=True, null=True, verbose_name='FECHA_MODIFICACION')),
                ('id_persona_rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.persona_rol', verbose_name='ID_PERSONA_ROL')),
            ],
            options={
                'db_table': 'PUBLICACION',
            },
        ),
        migrations.AddField(
            model_name='persona_rol',
            name='id_rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.rol', verbose_name='ID_ROL'),
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