# Generated by Django 4.0.3 on 2022-03-28 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0006_remove_post_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='descripcion',
        ),
    ]