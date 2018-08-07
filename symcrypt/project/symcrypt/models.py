from django.db import models
from project import settings
from django.contrib.auth.models import User


class Sms(models.Model):
    print("dakhele sms")
    sms_code = models.IntegerField()
    phone_number = models.CharField(max_length=30)
  

class TokenPhone(models.Model):

    phone_number = models.CharField(max_length=30)
    token = models.CharField(max_length=200)


class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
