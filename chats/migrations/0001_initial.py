# Generated by Django 4.0 on 2022-11-29 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=12)),
                ('groupId', models.CharField(max_length=12)),
                ('receiver', models.CharField(max_length=12)),
                ('Text', models.CharField(max_length=122, null=True)),
                ('Audio', models.CharField(max_length=122, null=True)),
            ],
        ),
    ]
