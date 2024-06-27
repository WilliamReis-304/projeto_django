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