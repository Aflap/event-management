from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('events/',views.events,name='events'),
    path('booking/',views.booking,name='booking'),
    path('contact/',views.contact,name='contact'),
    path('confirm/',views.confirm,name='confirm'),
    path('thanks/',views.thanks,name='thanks'),
    
    ]