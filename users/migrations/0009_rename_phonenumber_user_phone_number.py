# Generated by Django 4.2.16 on 2024-11-19 20:49

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_alter_user_avatar"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="phoneNumber",
            new_name="phone_number",
        ),
    ]
