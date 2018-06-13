from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RegistrarUserForm

#Telas iniciais

class Index(TemplateView):
    template_name = 'base.html'

class Login(TemplateView):
    template_name = 'login.html'

class UserCreateView(CreateView):
    model = User
    template_name = 'form.html'
    form_class = RegistrarUserForm

    # Como enviar outros dados para tela
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Login'
        context['input'] = 'Enviar'
        return context

class TurmasTemplateView(TemplateView): #Tela de turmas do disponiveis para o usuario - pos login
    template_name = 'turmas.html'
    login_url = '/entrar/'

    # Como enviar outros dados para tela
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Listar somente a turma
        context['turmas'] = models.Turma.objects.all()
        context['titulo'] = 'Lista de Turmas'
        return context

class TurmasCreateView(CreateView):
    model = models.Turma
    template_name = 'form.html'
    login_url = '/entrar/'
    fields = [
        'nome',
        'colegio'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastro de Turma'
        context['input'] = 'Cadastrar'

        return context

#Tela de Turma
class TurmaTemplateView(TemplateView): #Tela da turma que foi selecionada
    template_name = 'turma.html'
    login_url = '/entrar/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Turmas'
        return context

class AvisoCreateView(CreateView):
    template_name = 'form.html'
    model = models.Aviso
    login_url = '/entrar/'
    fields = [
        'data_final',
        'tipo_aviso',
        'comentarios'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastrar aviso'
        context['input'] = 'Adicionar'
        return context

class AlunosCreateView(CreateView):
    template_name = 'form.html'
    model = models.Turma
    login_url = '/entrar/'
    fields = [
        'nome',
        'colegio'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastro de Turma'
        context['input'] = 'Adicionar'
        return context

class InfoTurma(TemplateView): #Info da turma selecionada por meio de um botao na tela Turma
    template_name = 'infoturma.html'
    login_url = '/entrar/'
