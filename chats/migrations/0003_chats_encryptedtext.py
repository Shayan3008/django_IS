# Generated by Django 4.0 on 2022-12-01 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_keyroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='chats',
            name='EncryptedText',
            field=models.CharField(max_length=122, null=True),
        ),
    ]
