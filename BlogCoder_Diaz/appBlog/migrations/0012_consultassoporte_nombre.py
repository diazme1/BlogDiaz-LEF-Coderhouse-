# Generated by Django 4.0.3 on 2022-03-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0011_consultassoporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultassoporte',
            name='nombre',
            field=models.CharField(default=' ', max_length=30),
            preserve_default=False,
        ),
    ]
