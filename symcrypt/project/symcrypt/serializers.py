# from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User 
from symcrypt.models import Sms
# from phonenumber_field.modelfields import PhoneNumberField


class UserSerializer(serializers.ModelSerializer):

    phone_number = serializers.CharField(required=True, source='username')
    email = serializers.EmailField(required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
                               )
    password = serializers.CharField(min_length=8, write_only=True)
  
    class Meta:
            model = User
            fields = ('phone_number', 'email', 'password')

    def create(self, validated_data):
        #print(validated_data)
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        #print(user)
        return user

class SmsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sms
        fields = ('sms_code', 'phone_number')

    #def create(self, validated_data)
    #    return Sms.objects.create(**validated_data)

    
"""class VerificationSerializer(serializers.ModelSerializer):

      sms_code = serializers.IntegerField(required=True)
      phone_number = serializers.CharField(required=True)

        class Meta:
            model = User
            fields = ('sms_code', 'phone_number')
        def create(self, validated_data):
            print(validated_data)"""
