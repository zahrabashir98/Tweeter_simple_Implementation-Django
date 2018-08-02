from rest_framework import serializers
from polls.models import TweetModel
from django.contrib.auth.models import User

class TweetModelSerializer (serializers.ModelSerializer):
    class Meta :
        model =TweetModel
        fields = ('text' ,'userID', 'date')

    def create(self, validated_data):
       
        return TweetModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
    
        instance.text = validated_data.get('title', instance.text)
        instance.userID = validated_data.get('code', instance.userID)
        instance.date = validated_data.get('linenos', instance.date)
        instance.save()
        return instance
class LoginModelSeializer (serializers.ModelSerializer):
    class Meta :
        model= User
        fields =('username', 'password')

class UserSeializer(serializers.ModelSerializer):
    tweetmodels=serializers.PrimaryKeyRelatedField(many =True , queryset=TweetModel.objects.all())

    class Meta :
        model = User
        fileds= ('userID' , 'Text' , 'tweetmodels')