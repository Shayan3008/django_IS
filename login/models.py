from django.db import models

# Create your models here.
class chatUsers(models.Model):
    email = models.CharField(max_length=122,unique=True)
    password = models.CharField(max_length=12)
    name = models.CharField(max_length=122,null=True)
    privKey = models.CharField(max_length=1025,null=True)
    pubKey = models.CharField(max_length=1025,null=True)