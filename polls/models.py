from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TweetModel(models.Model):
    text = models.CharField(max_length=200)
    #owner =models.ForeignKey('auth.user' , on_delete=models.CASCADE)
    #id =models.CharField()
    
    userr = models.ForeignKey(User, on_delete=models.CASCADE )
    print("yoyuhphppppp") 
    
   # date = models.DateField(auto_now_add= True )
    def __str__(self):
        return self.text
    class Meta :
        ordering = ('text',)