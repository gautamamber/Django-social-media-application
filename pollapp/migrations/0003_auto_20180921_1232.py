# Generated by Django 2.0.2 on 2018-09-21 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
