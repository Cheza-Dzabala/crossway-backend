# Generated by Django 5.1.1 on 2024-11-19 18:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_user_avatar"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="lattitude",
        ),
        migrations.RemoveField(
            model_name="user",
            name="longitude",
        ),
    ]
