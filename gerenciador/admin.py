from django.contrib import admin
from .models import Cursos,Alunos
# Register your models here.

class AdminCursos(admin.ModelAdmin):
    ...

@admin.register(Alunos)
class AdminAlunos(admin.ModelAdmin):
    ...

admin.site.register(Cursos,AdminCursos)