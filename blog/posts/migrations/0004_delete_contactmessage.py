# Generated by Django 5.1.7 on 2025-06-22 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_contactmessage"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ContactMessage",
        ),
    ]
