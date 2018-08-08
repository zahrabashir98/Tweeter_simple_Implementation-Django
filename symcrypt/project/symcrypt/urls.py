from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^upload/$', views.FileView.as_view(), name='file-upload'),
   # url(r'api/users^$', views.UserCreate.as_view(), name='signup'),
] 