# Generated by Django 2.0.2 on 2018-10-09 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0015_facts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
    ]
