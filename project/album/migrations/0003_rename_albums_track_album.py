# Generated by Django 4.2.3 on 2023-07-04 00:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_remove_track_album_track_albums'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='albums',
            new_name='album',
        ),
    ]
