# Generated by Django 4.2.16 on 2024-11-28 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("drivers", "0007_alter_driver_ban_reason"),
        ("vehicles", "0004_alter_vehicle_license_plate"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="driver",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="vehicles",
                to="drivers.driver",
            ),
        ),
    ]
