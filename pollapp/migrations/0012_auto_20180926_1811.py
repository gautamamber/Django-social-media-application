# Generated by Django 2.0.2 on 2018-09-26 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0011_auto_20180926_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aa', to='pollapp.Post'),
        ),
    ]
