from django.contrib.auth.models import User
from rest_framework import serializers

from polls.models import TweetModel

class TweetModelSerializer (serializers.ModelSerializer ):
   
    class Meta :
        model =TweetModel
        fields = ('text',)

    def delete(self ,instance,pk, validated_data):
        instance.delete(**validated_data)

        

    def create(self, validated_data):
        return TweetModel.objects.create(**validated_data)


    def update(self, instance, validated_data):

        instance.text = validated_data.get('text', instance.text)
      #  instance.userID = validated_data.get('code', instance.userID)
       # instance.date = validated_data.get('linenos', instance.date)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    Tweets = serializers.PrimaryKeyRelatedField(many=True, queryset=TweetModel.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'Tweets')