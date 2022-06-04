from django.urls import path

from quickstart import  views

urlpatterns=[

    path('',views.home,name='home'),  
    path('addemp',views.addemp,name='addemp')
    ]