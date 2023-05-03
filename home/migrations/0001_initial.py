# Generated by Django 4.2 on 2023-05-03 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.CharField(max_length=600)),
            ],
        ),
    ]
