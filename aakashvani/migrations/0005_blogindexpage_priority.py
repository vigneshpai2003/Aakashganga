# Generated by Django 3.2.11 on 2022-01-13 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aakashvani', '0004_delete_blogpagegalleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='priority',
            field=models.IntegerField(default=1),
        ),
    ]