from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TweetModel(models.Model):
    text = models.CharField(max_length=200)
    #id =models.CharField()
   # userID =models.ForeignKey(User, on_delete=models.CASCADE)
   # date = models.DateField(auto_now_add= True )
    def __str__(self):
        return self.text
    class Meta :
        ordering = ('text',)