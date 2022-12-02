from django.db import models

# Create your models here.


class Chats(models.Model):
    sender = models.CharField(max_length=12)
    groupId = models.CharField(max_length=12)
    receiver = models.CharField(max_length=12)
    Audio = models.CharField(max_length=122, null=True)
    EncryptedText = models.CharField(max_length=1000, null=True)


class KeyRoom(models.Model):
    groupId = models.CharField(max_length=50)
    key = models.CharField(max_length=50)
