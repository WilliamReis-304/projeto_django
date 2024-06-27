from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cursos(models.Model):
    nome_curso = models.CharField(max_length=100)
    valor_matricula = models.IntegerField()
    data_de_inicio = models.DateField(auto_now=True)
    hora_da_aula = models.TimeField()
    
    def __str__(self) -> str:
        return self.nome_curso

class Alunos(models.Model):
    nome_aluno = models.CharField(max_length=100)
    idade_aluno = models.IntegerField()
    # curso = models.ForeignKey(Cursos,on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.nome_aluno