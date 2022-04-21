from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'auth0'

urlpatterns = [
    path('signup/', views.signup, name ='signup'),
    path('signin/', views.signin, name = 'login'),
    path('signout/', views.signout, name = 'logout'),
]
