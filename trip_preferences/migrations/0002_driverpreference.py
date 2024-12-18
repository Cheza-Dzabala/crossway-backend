# Generated by Django 4.2.16 on 2024-11-27 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("drivers", "0007_alter_driver_ban_reason"),
        ("trip_preferences", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="DriverPreference",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "driver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="preferences",
                        to="drivers.driver",
                    ),
                ),
                (
                    "preference",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="driver_preferences",
                        to="trip_preferences.trippreferences",
                    ),
                ),
            ],
        ),
    ]
