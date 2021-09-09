from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contacts',views.contacts,name='contacts'),
    path('signup',views.Handlesignup,name='Handlesignup'),
    path('login',views.Handlelogin,name='Handlelogin'),
    path('logout',views.Handlelogout,name='Handlelogout'),
    path('search',views.search,name='search'),
]