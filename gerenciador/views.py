from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    return render(request,"gerenciador/paginas/index.html")

def lista_alunos(request):
    lista_de_alunos =Alunos.objects.all()
    contexto = {'lista_de_alunos':lista_de_alunos}
    return render(request,"gerenciador/paginas/lista_de_alunos.html",context=contexto)

def lista_cursos(request):
    lista_de_cursos =Cursos.objects.all()
    contexto = {'lista_de_cursos':lista_de_cursos}
    return render(request,"gerenciador/paginas/lista_de_cursos.html",context=contexto)

def cadastrar_aluno(request):
    if request.method == "POST":
        form=formAlunos(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = formAlunos()
    contexto = {'form':form}
    return render(request,"gerenciador/paginas/cadastrar_aluno.html",context = contexto)

def cadastrar_curso(request):
    if request.method == "POST":
        form=formCursos(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = formCursos()
    contexto = {'form':form}
    return render(request,"gerenciador/paginas/cadastrar_curso.html",context = contexto)