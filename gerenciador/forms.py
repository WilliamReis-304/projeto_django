from django import forms
from .models import *

class formAlunos(forms.ModelForm):
    class Meta:
        model = Alunos
        fields = ["nome_aluno","idade_aluno"]
        widgets = {
            "nome_aluno":forms.TextInput(attrs={"class":"class_forms"}),
            "idade_aluno":forms.NumberInput(attrs={"class":"class_forms"})
        }
class formCursos(forms.ModelForm):
    class Meta:
        model = Cursos
        fields = ["nome_curso", "valor_matricula", "data_de_inicio", "hora_da_aula"]
        widgets = {
            "nome_curso":forms.TextInput(),
            "valor_matricula":forms.NumberInput(),
            "data_de_inicio": forms.DateInput(),
            "hora_da_aula":forms.TimeInput(),
        }