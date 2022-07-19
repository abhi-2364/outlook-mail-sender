from django.contrib import admin
from django.urls import path,include
from mailapp import views
urlpatterns = [
    path('',views.html),
    path('mail',views.mail)
]