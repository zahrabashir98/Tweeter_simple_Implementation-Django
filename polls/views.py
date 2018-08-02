from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import login
from polls.forms import TwittForm
from datetime import datetime
from polls.models import TweetModel
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from polls.serializers import TweetModelSerializer,LoginModelSeializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# Create your views here.

class LoginView(APIView):

    def post (self , request , format = None):
        serializer= LoginModelSeializer(data=request.data)
        if serializer.is_valid():
            user=request.user
            print(user)
            login(request,user)
            u = User.objects.all()
            print(u)
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response (serializer.errors , status =status.HTTP_400_BAD_REQUEST)

    


class TweeterPage(APIView):
    @login_required
    def post(self , request ,format= None):
        serializer=TweetModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response (serializer.errors , status =status.HTTP_400_BAD_REQUEST)
   # @login_required
    def get(self, request, format=None):
        tweetmodels = TweetModel.objects.all()
        serializer = TweetModelSerializer(tweetmodels, many=True)
        print(request.user)
        return Response(serializer.data)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TweeterPage, self).dispatch(*args, **kwargs)
   
            
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