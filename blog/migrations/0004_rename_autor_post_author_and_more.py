# Generated by Django 4.2 on 2023-06-21 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_author_post_autor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autor',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='contenido',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='imagen',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='titulo',
            new_name='title',
        ),
    ]
