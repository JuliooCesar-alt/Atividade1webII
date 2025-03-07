from django.contrib import admin
from django.urls import path
from calculadora import views
from django.urls import path, include
from django.contrib.auth import authenticate, login

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('index/', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('soma/', views.soma, name='soma'),
    path('divisao/', views.divisao, name='divisao'),
    path('subtrair/', views.subtrair, name='subtrair'),
    path('multiplicar/', views.multiplicar, name='multiplicar'),
    path('autor/', views.autor, name='autor'),
    path('enquete/', views.enquete, name='enquete'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
]
