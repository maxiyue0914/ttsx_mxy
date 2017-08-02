from django.db import models


# Create your models here.
class user_info(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=20)
    ushou = models.CharField(max_length=20, default='')
    uaddr = models.CharField(max_length=100, default='')
    utel = models.CharField(max_length=11, default='')
