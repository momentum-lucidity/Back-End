# Generated by Django 3.2.6 on 2021-08-15 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20210814_1855'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alert',
            old_name='title',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='title',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='title',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='note',
            old_name='note_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='statusbar',
            old_name='unfinished',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='text',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='volunteerslot',
            old_name='text_slot',
            new_name='id',
        ),
    ]
