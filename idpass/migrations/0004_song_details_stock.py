# Generated by Django 4.0.2 on 2022-05-05 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idpass', '0003_song_details_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='song_details',
            name='stock',
            field=models.IntegerField(default=3),
        ),
    ]
