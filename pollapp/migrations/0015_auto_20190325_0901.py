# Generated by Django 2.0 on 2019-03-25 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0014_electionupdate_total_no_of_seats'),
    ]

    operations = [
        migrations.AddField(
            model_name='electionupdate',
            name='result',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='electionupdate',
            name='total_no_of_seats',
            field=models.IntegerField(blank=True),
        ),
    ]