# Generated by Django 4.1.3 on 2022-11-21 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0002_alter_chatusers_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatusers",
            name="email",
            field=models.CharField(max_length=125, unique=True),
        ),
    ]
