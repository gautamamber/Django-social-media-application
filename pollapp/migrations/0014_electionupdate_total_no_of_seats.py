# Generated by Django 2.0 on 2019-03-25 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0013_auto_20190325_0754'),
    ]

    operations = [
        migrations.AddField(
            model_name='electionupdate',
            name='total_no_of_seats',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
