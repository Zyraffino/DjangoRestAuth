from django.contrib import admin
from django.urls import path, include
from .views import landing

urlpatterns = [
    path('', landing, name='landing'),
]
