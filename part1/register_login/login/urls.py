# TODO напишите здесь url для получения токена
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('login/', views.obtain_auth_token),
]
