from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('',views.register,name='register'),
    path('login_user',views.login_user,name='login_user'),
    path('signout',views.signout,name='signout'),
    path('main', views.mainpg, name="mainpg"),
    path('about', views.about, name="about"),
    path('booking', views.booking, name="booking"),
    path('contact', views.contact, name="contact"),
    path('error404',views.error,name="error"),
    path('feedback',views.feedback,name="feedback"),
    path('confirmation',views.confirmation,name="confirmation"),
    path('appoint.html',views.appoint,name="appoint"),
]

