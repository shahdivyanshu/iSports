from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.bloghome,name='bloghome'),
    path('createblog',views.createblog,name='bloghome'),
    path('userblogs',views.userblogs,name="userblogs"),
    path('postcomment',views.postcomment,name="postcomment"),
    path('<str:slug>',views.blogPost,name='blogPost')
]