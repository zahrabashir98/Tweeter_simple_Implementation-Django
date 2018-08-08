from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^upload/$', views.FileView.as_view(), name='file-upload'),
]