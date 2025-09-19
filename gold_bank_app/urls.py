from django.contrib import admin
from django.urls import path
from . import views

app_name = 'gold_bank_app'

urlpatterns =[
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login')

]