# Generated by Django 4.2 on 2023-06-22 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_comments',
            field=models.ManyToManyField(related_name='post_comments', to='blog.comment'),
        ),
    ]