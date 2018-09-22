from django.db import models
from django.contrib.auth.models import User
from django.contrib import auth
# Create your models here.
"""class users(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=20)
    
    def __str__(self):
        return self.username"""
    
    
class Devices(models.Model):
    #id=models.ForeignKey(User,on_delete=models.CASCADE)
    devicename=models.CharField(max_length=20)
    devicemodel=models.CharField(max_length=10)
    devicedsc=models.CharField(max_length=50)
    devicestatus=models.CharField(max_length=10)
    class Meta:
        db_table="devices"
    
   