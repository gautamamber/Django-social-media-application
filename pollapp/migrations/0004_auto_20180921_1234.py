# Generated by Django 2.0.2 on 2018-09-21 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0003_auto_20180921_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='New/%Y/%m/%d'),
        ),
    ]
