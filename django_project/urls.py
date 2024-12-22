from django.contrib import admin
from django.urls import path
from calculadora import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AlunoViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)

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
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
