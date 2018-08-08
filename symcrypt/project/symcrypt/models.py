from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    print(type(user))
    phone_number = models.CharField(max_length=500, blank=True)
    pre_phone = models.CharField(max_length=500, blank=True)
    sms_code = models.CharField(max_length=300, blank=True)
    token = models.CharField(max_length=60, blank=True)
    pic = models.ImageField(upload_to='images/', default='images/img.jpg')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print("jfksnef")
        Profile.objects.create(user=instance)
        print("bade in")


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    print("too update")
    instance.profile.save()
    print("bade update")


class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class File(models.Model):
    file = models.FileField(blank=False, null=False)
