from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.Home,name='index'),
    path('register',views.register,name='register'),
    # path('login',views.demo2,name='login'),
    path('login', views.login, name='login'),
    path('logout',views.logout,name="logout"),
    path('booking',views.booking,name="booking"),
    path('appo',views.appo,name='appo')

]
