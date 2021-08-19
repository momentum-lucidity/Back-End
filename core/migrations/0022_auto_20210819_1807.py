# Generated by Django 3.2.6 on 2021-08-19 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20210819_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteerslot',
            name='timespan',
        ),
        migrations.AddField(
            model_name='volunteerslot',
            name='endtime',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volunteerslot',
            name='starttime',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
