# Generated by Django 3.2.11 on 2022-01-13 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aakashvani', '0007_blog_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]
