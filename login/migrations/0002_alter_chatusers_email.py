# Generated by Django 4.1.3 on 2022-11-20 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chatusers",
            name="email",
            field=models.CharField(max_length=122, unique=True),
        ),
    ]
