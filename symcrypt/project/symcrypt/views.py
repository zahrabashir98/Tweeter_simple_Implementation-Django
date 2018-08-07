from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from symcrypt.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from symcrypt.models import Sms ,TokenPhone , Contact
import random
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import uuid 





class UserCreate(APIView):
    """ 
    Creates the user. 
    """

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            print (type(request.data))
            #Sms.user=request.user
            sms = Sms(sms_code= generate(), phone_number=request.data['phone_number'])
            table = TokenPhone()
            print(sms.phone_number)
            #print(sms.objects.all())
            sms.save()
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response (serializer.errors ,status=status.HTTP_400_BAD_REQUEST)


def generate():
    print("dakhele generate")
    r = random.randint(1000,10000)
    Sms.sms_code = r
    #print(Sms.sms_code)
    return r 
        

class Verification(APIView):
    
    def post(self,request,format='json'):
        sms=Sms.objects.get(phone_number=request.data['phone_number'])
        print(type(sms.sms_code))
        print("*************************")
        print(type(request.data['sms_code']))
        if(sms.sms_code==int(request.data['sms_code'])):
            print("here")
            return Response({"message":"verified"},status=status.HTTP_200_OK)
    
        else:
            return Response({"message":"Wrong code"},status=status.HTTP_400_BAD_REQUEST)
    

class ForgetPassword(APIView):
    def post(self,request, format='json'):
        t = TokenPhone(phone_number=request.data['phone_number'] , token=uuid.uuid4() )
        t.save()
        return Response({"message":"Ok , now check your"},status=status.HTTP_200_OK)


class SetNewPassword(APIView):
    def post(self, request, format='json'):
        t = TokenPhone.objects.get(phone_number=request.data['phone_number'])
        if request.data['token']==t.token :
            print("equal")
            user = User.objects.get(username=request.data['phone_number'])
            user.password=request.data['password']
            user.save()
            return Response({"message":"successfuly changed"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":"wrong url"},status=status.HTTP_404_NOT_FOUND)

 
class ContactView(APIView):

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format='json'):
        print("sfbjhbsakcbkanckan")
        print(request.user)
        for contact in request.data["contacts"]:
            u= Contact(name=contact['name'] , phone_number = contact['phone_number'] , user=request.user)
            u.save()
        return Response({"message":"successfuly changed"}, status=status.HTTP_200_OK)
