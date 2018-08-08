from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from symcrypt.models import Contact, Profile
import random
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import uuid
from rest_framework.parsers import MultiPartParser, FormParser


class UserCreate(APIView):
    """
        asdasdasd
    """

    def post(self, request, format='json'):
        """
        post
        """
        print("inja")
        userr = User(username=request.data['username'])
        userr.set_password(request.data['password'])
        userr.save()
        userr.profile.phone_number = request.data['phone_number']
        userr.profile.sms_code = str(random.randint(1000, 10000))
        userr.profile.save()
        print(userr.profile)
        if userr:
            return Response({"message": "user created"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "couldnt make"}, status=status.HTTP_400_BAD_REQUEST)


class Verification(APIView):

    def post(self, request, format='json'):
        user = Profile.objects.get(phone_number=request.data['phone_number'])
        print(user.sms_code)
        print(request.data['sms_code'])
        print(user.pic)
        if user.sms_code == request.data['sms_code']:
            print("here")
            return Response({"message": "verified"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Wrong code"}, status=status.HTTP_400_BAD_REQUEST)


class Update(APIView):
    """
    SFA
    """

    def post(self, request, format='json'):
        userr = Profile.objects.get(phone_number=request.data['pre_phone'])
        userr.phone_number = request.data['phone_number']
        request.user.username = request.data['username']
        request.user.email = request.data['email']
        request.user.save()
        userr.save()
        print(userr)
        return Response({"message": "done"}, status=status.HTTP_200_OK)


class GetImage(APIView):

    def post(self, request, format='json'):
        user = Profile.objects.get(phone_number=request.data['phone_number'])
        user.pic = request.FILES.get('img')
        print(user.pic)
        user.save()
        return Response({"message": "done"}, status=status.HTTP_200_OK)


class ForgetPassword(APIView):
    def post(self, request, format='json'):
        user = Profile.objects.get(phone_number=request.data['phone_number'])
        user.token = uuid.uuid4()
        user.save()
        return Response({"message": "Ok , now check your"}, status=status.HTTP_200_OK)


class SetNewPassword(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format='json'):
        user = Profile.objects.get(phone_number=request.data['phone_number'])

        if request.data['token'] == user.token:
            print("equal")
            print(request.user.password)
            request.user.set_password(request.data['password'])
            print(request.user.password)
            request.user.save()
            print()
            user.save()
            return Response({"message": "successfuly changed"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "wrong url"}, status=status.HTTP_404_NOT_FOUND)


class ContactView(APIView):

    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format='json'):
        print("sfbjhbsakcbkanckan")
        print(request.user)
        for contact in request.data["contacts"]:
            u = Contact(
                name=contact['name'], phone_number=contact['phone_number'], user=request.user)
            u.save()
        if u:
            return Response({"message": "successfuly changed"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "sth went wrong!!!"}, status=status.HTTP_400_BAD_REQUEST)


class FileView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(
                file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
