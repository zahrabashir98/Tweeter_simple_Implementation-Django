from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect,HttpResponse

from django.utils.decorators import method_decorator
from django.http import Http404

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from polls.forms import TwittForm
from datetime import datetime
from polls.models import TweetModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from polls.serializers import TweetModelSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class TweeterPage(APIView):
    #@login_required
 
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def get_object(self, id):
        try:
            return TweetModel.objects.get(id=id)
        except TweetModel.DoesNotExist:
            raise Http404

    def post(self , request ,format= None):
        serializer=TweetModelSerializer(data=request.data)
        if serializer.is_valid():
            print("dakheele vlidated ")
            #print(dir(serializer))
            #serializer.validated_data['userr']=request.user
            #print(serializer.validated_data)
            #u = User.objects.filter(id=1).first()
            print(request.user)
            serializer.save(userr=request.user)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST)
   
    def delete(self, request, format=None):
        print(request.data['id'])
        tweet_object = self.get_object(request.data['id'])
        if request.user==tweet_object.userr:
            deleted.delete()
            return Response({"message": "tweet deleted"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {
                    "message": "the access is denied ,"\
                    "you cant delete other users' tweets "
                },
                status=status.HTTP_403_FORBIDDEN
            )

    def get(self, request, format=None): 
        tweetmodels = TweetModel.objects.all()
        serializer = TweetModelSerializer(tweetmodels, many=True)
        print(request.user)
        return Response(serializer.data)

    def put(self, request, format=None):
        tweetmodels = self.get_object(request.data['id'])
        serializer = TweetModelSerializer(tweetmodels, data=request.data)
        if serializer.is_valid():
            serializer.save()
           # return Response(serializer.data)
        if serializer.errors :
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"updated" }, status=status.HTTP_200_OK)



"""
def login_view(request):

   
    if request.method== 'POST' :
    
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            #return HttpResponse("hello")
            #return render(request,"polls/main.html",{'user': user})
            #return render(request,'twitForms.html' ,{'form':TwittForm})
            return HttpResponseRedirect('/twitter/' )
    else:
        form=AuthenticationForm()
    
    #return HttpResponse("hello")
    return render(request,"polls/login.html",{'form': form})

@login_required
def TwitterPage(request):
    
    
    if request.method=='POST':
        form=TwittForm(request.POST)
        print(form)
        print(dir(form))
        data=form.cleaned_data['textfield']
        m = TweetModel(text=data  , userID=request.user )
        m.save()
        if form.is_valid():
           
            #now = datetime.utcnow() --> instead of auto ...
            print(request.user)
            
            print(TweetModel.objects.all())
            
            #print(m.objects.all())
            #return render(request,'twitForms.html',{'user':request.user , 'text': data , 'alltexts': TweetModel.objects.all() })
            return HttpResponseRedirect('')
            #redirect to this page
         #  return render(request,'twitForms.html' ,{'form':form})
     
    form=TwittForm(request.GET)

    return render(request,'twitForms.html' ,{'form':form ,'user':request.user , 'text': '' , 'alltexts': TweetModel.objects.all() })
"""
