# Generated by Django 5.1.1 on 2024-11-19 13:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[],
        ),
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=100),
        ),
    ]
