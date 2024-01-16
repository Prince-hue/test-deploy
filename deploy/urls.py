from django.urls import path
from . import views

#URLConf
urlpatterns = [
    #path("", views.index, name='indexx'),
    path("deployy/", views.deployy, name='deployy'),
    
]

