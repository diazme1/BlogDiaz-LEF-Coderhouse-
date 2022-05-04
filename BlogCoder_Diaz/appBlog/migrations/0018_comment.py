# Generated by Django 4.0.3 on 2022-04-30 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0017_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('post', models.CharField(max_length=100)),
            ],
        ),
    ]
