from django.urls import path

from quickstart import  views

urlpatterns=[

    path('',views.home,name='home'),  
    path('add',views.add,name='add')
    ]