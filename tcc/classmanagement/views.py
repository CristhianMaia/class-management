from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import RegistrarUserForm

#Telas iniciais

class Index(TemplateView):
    template_name = 'base.html'

#------------CreateView--------------#
class UserCreateView(CreateView):
    model = User
    template_name = 'form.html'
    form_class = RegistrarUserForm
    success_url = reverse_lazy('index') # pra onde ir depois de cadastrar

    # Como enviar outros dados para tela
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Registrar-se como Aluno'
        context['input'] = 'Enviar'
        return context


class TurmaCreateView(LoginRequiredMixin, CreateView): #Tela de crianção de turmas
    model = models.Turma
    template_name = 'form.html'
    login_url = '/login/'
    success_url = reverse_lazy('index') # pra onde ir depois de cadastrar
    fields = [
        'nome',
        'alunos',
        'representante',
        'colegio'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastro de Turma'
        context['input'] = 'Cadastrar'
        return context


class ProfessorCreateView(LoginRequiredMixin, CreateView):  # Cadastro de Professores
    template_name = 'form.html'
    model = models.Professor
    login_url = '/login/'
    success_url = reverse_lazy('index')  # pra onde ir depois de cadastrar
    fields = [
        'nome',
        'email'
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastro de Professores'
        context['input'] = 'Adicionar Professor'
        return context


class ColegioCreateView(LoginRequiredMixin, CreateView):  # Cadastro de Professores
    template_name = 'form.html'
    model = models.Colegio
    login_url = '/login/'
    success_url = reverse_lazy('index')  # pra onde ir depois de cadastrar
    fields = [
        'nome'
    ]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastro de Colegios'
        context['input'] = 'Adicionar Colegio'
        return context


class MateriaCreateView(LoginRequiredMixin, CreateView): #Cadastro de Materias
    template_name = 'form.html'
    model = models.Materia
    login_url = '/login/'
    success_url = reverse_lazy('index')
    fields = [
        'nome',
        'local',
        'dia',
        'horario_inicio',
        'horario_fim',
        'turma',
        'professor'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastro de Materias'
        context['input'] = 'Adicionar Matéria'
        return context


class AtendimentoCreateView(LoginRequiredMixin, CreateView): #Cadastro de atendimentos
    template_name = 'form.html'
    model = models.Atendimento
    login_url = '/login/'
    success_url = reverse_lazy('index')
    fields = [
        'turma',
        'professor',
        'dia',
        'horario_inicio',
        'horario_fim'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastro de Atendimento'
        context['input'] = 'Adicionar Atendimento'
        return context

class AvisoCreateView(LoginRequiredMixin, CreateView):  #Cadastro de Aviso
    template_name = 'form.html'
    model = models.Aviso
    login_url = '/login/'
    success_url = reverse_lazy('index')
    fields = [
        'turma',
        'materia',
        'tipo_aviso',
        'comentarios',
        'data_final'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastrar aviso'
        context['input'] = 'Adicionar'
        return context


# --------------- FIM DOS CADASTROS ---------------------#

#---------------- TemplateView -------------------#
class Login(TemplateView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Login'
        return context


class TurmasTemplateView(LoginRequiredMixin, TemplateView): #Tela de turmas do disponiveis para o usuario - pos login
    template_name = 'turmas.html'
    login_url = '/login/'

    # Como enviar outros dados para tela
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Listar somente a turma
        context['turmas'] = models.Turma.objects.all()
        context['titulo'] = 'Lista de Turmas'
        return context


class TurmaTemplateView(LoginRequiredMixin,TemplateView): #Tela da turma que foi selecionada
    template_name = 'turma.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = '%TurmaNome%'
        return context


#-----------------------ListView--------------------------#
class HorariosTemplateView(LoginRequiredMixin,TemplateView): #Tela da turma que foi selecionada
    template_name = 'horarios.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Horarios de Aula'
        return context


class AtendimentosTemplateView(LoginRequiredMixin,TemplateView): #Tela da turma que foi selecionada
    template_name = 'atendimentos.html'
    login_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atendimentos'
        return context


class InfoTurma(LoginRequiredMixin, TemplateView): #Info da turma selecionada por meio de um botao na tela Turma
    template_name = 'infoturma.html'
    login_url = '/login/'



#-----------------lixo---------------#
class AlunosCreateView(LoginRequiredMixin, CreateView): #Cadastro de Alunos
    template_name = 'form.html'
    model = models.Turma
    login_url = '/login/'
    fields = [
        'nome',
        'colegio'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastro de Turma'
        context['input'] = 'Adicionar Aluno'
        return context



