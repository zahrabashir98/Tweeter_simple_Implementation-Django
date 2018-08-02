from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from polls import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view()),
    url(r'^tweeter/$', views.TweeterPage.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)


   #url(r'^login/$', login, {'template_name': 'polls/login.html'}, name='login'),
    #url(r'^login/$',login_view, name='login')