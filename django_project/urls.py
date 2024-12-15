from django.contrib import admin
from django.urls import path
from calculadora import views

urlpatterns = [
    path('', views.vazio, name='vazio'),# Página inicial
    path('vazio', views.home, name='home'),  
    path('soma/', views.soma, name='soma'),                                            path('divisao/', views.divisao, name='divisao'),
    path('subtrair/', views.subtrair, name='subtrair'),
    path('multiplicar/', views.multiplicar, name='multiplicar'),  
    path('autor/', views.autor, name='autor'),
    ]
