from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.utils import timezone
from .models import Alunos

# Create your views here.
#TODO: deixar a media automatica
class AlunosCreate(CreateView):
    model = Alunos
    fields = ['nome', 'sobrenome', 'nota1', 'nota2', 'nota3','media','idade', 'obs']
    success_url = '/alunos/list'

class AlunosList (ListView):
    model= Alunos

class AlunosDetail (DetailView):
    model = Alunos

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class AlunosUpdate(UpdateView):
    model = Alunos
    fields = ['nome', 'sobrenome', 'nota1', 'nota2', 'nota3','media','idade', 'obs']
    success_url = '/alunos/list'

class AlunosDelete(DeleteView):
    model = Alunos
    success_url = '/alunos/list'
