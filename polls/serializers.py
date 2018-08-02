from django.contrib.auth.models import User
from rest_framework import serializers

from polls.models import TweetModel



class TweetModelSerializer (serializers.ModelSerializer ):
   
    class Meta :
        model =TweetModel
        fields = "__all__"

    def delete(self ,instance,pk, validated_data):
        instance.delete(**validated_data)
        

    def create(self, validated_data):
        return TweetModel.objects.create(**validated_data)

    def update(self, instance, validated_data):

        instance.text = validated_data.get('text', instance.text)
       # instance.userID = validated_data.get('code', instance.userID)
       # instance.date = validated_data.get('linenos', instance.date)
        instance.save()
        return instance


class LoginModelSerializer (serializers.ModelSerializer):
    class Meta :
        model= User
        fields =('username', 'password')

"""
'userID', 'date'

    class UserSeializer(serializers.ModelSerializer):
        tweetmodels=serializers.PrimaryKeyRelatedField(many =True , queryset=TweetModel.objects.all())

        class Meta :
            model = User
            fileds= ('userID' , 'Text' , 'tweetmodels')"""