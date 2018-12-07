from django.forms import ModelForm
from .models import Alunos


class AlunosForm(ModelForm):
    class Meta:
        model = Alunos
        fields = ['nome', 'sobrenome', 'nota1', 'nota2', 'nota3', 'media','idade', 'obs']