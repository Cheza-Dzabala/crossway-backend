# Generated by Django 4.2.16 on 2024-11-19 20:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vehicles", "0003_alter_vehicle_driver"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="license_plate",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
