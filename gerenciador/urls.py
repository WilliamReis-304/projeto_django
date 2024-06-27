from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('lista_de_alunos/', views.lista_alunos),
    path('cadastrar_aluno/', views.cadastrar_aluno),
]