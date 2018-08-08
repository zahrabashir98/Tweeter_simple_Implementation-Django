# from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User 
from .models import File

class UserSerializer(serializers.ModelSerializer):

    phone_number = serializers.CharField(required=True, source='username')
    email = serializers.EmailField(required=True,
        validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(min_length=8, write_only=True)


    class Meta:
            model = User
            fields = ('phone_number', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        #print(user)
        return user

    class FileSerializer(serializers.ModelSerializer):
        class Meta():
            model = File
            fields = ('file',)