# Generated by Django 4.2.16 on 2024-11-28 15:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rides", "0003_ride_is_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="ride",
            name="capacity",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
