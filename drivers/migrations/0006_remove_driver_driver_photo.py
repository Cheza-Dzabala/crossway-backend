# Generated by Django 4.2.16 on 2024-11-27 18:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("drivers", "0005_delete_driverapplication"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="driver",
            name="driver_photo",
        ),
    ]
