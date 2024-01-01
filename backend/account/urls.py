from .views import *
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('Register/',UserRegistrationView.as_view(),name='Registration')
]
