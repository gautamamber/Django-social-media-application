# Generated by Django 2.0 on 2019-03-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0004_auto_20190311_0600'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'News Letter',
                'verbose_name_plural': 'News Letter',
            },
        ),
    ]
