# Generated by Django 3.2.6 on 2021-08-11 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_statusbar_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address1',
            field=models.CharField(default='Address 1', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='address2',
            field=models.CharField(default='Address 2', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='availability',
            field=models.TextField(default='Availability', max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default='City', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='display_name',
            field=models.CharField(default='preferred name', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='intake_status',
            field=models.CharField(default='volunteer status', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='legal_name',
            field=models.CharField(default='full legal name', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='preferred_event',
            field=models.TextField(default='preferred events', max_length=500),
        ),
        migrations.AddField(
            model_name='user',
            name='pronouns',
            field=models.CharField(default='preferred pronouns', max_length=200),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default='State', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='telephone',
            field=models.CharField(default='10-digit phone number', max_length=250),
        ),
        migrations.AddField(
            model_name='user',
            name='user_status',
            field=models.CharField(default='permissions status', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='zipcode',
            field=models.CharField(default='Zipcode', max_length=10),
        ),
        migrations.AlterField(
            model_name='statusbar',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_status', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default='e-mail address', max_length=200, null=True),
        ),
    ]