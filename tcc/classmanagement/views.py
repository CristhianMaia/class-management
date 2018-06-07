from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin


#Telas iniciais

class Index(TemplateView):
    template_name = 'index.html'

#Telas iniciais pos-login
class TurmasTemplateView(TemplateView): #Tela de turmas do usuario - pos login
    template_name = 'turmas.html'
    login_url = '/entrar/'

    # Como enviar outros dados para tela
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Listar somente a turma
        context['turmas'] = models.Turma.objects.all()
        context['titulo'] = 'Lista de Turmas'
        return context

class CriacaoTurma(TemplateView): #Tela de criaao de turmas
    template_name = 'criacaoturma.html'
    login_url = '/entrar/'

#Tela de Turma
class Turma(TemplateView): #Tela da turma que foi selecionada
    template_name = 'turma.html'
    login_url = '/entrar/'

class InfoTurma(TemplateView): #Info da turma selecionada por meio de um botao na tela Turma
    template_name = 'infoturma.html'
    login_url = '/entrar/'

class UserCreateView(CreateView):
    model = User
    template_name = 'form.html'
    fields = [
        'first_name',
        'last_name',
        'email',
        'username',
        'password'
    ]

    # Como enviar outros dados para tela
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastro de alunos'
        return context