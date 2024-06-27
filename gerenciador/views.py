from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    return render(request,"gerenciador/paginas/index.html")

def lista_alunos(request):
    lista_de_alunos =Alunos.objects.all()
    contexto = {'lista_de_alunos':lista_de_alunos}
    return render(request,"gerenciador/paginas/lista_de_alunos.html",context=contexto)