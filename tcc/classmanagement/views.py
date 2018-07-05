from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import RegistrarUserForm

#Telas iniciais

class Index(TemplateView,#AnonymousRequiredMixin
            ):
    template_name = 'base.html'
    authenticated_redirect_url = '/turmas'

#------------CreateView--------------#
class UserCreateView(CreateView, #AnonymousRequiredMixin
                     ):
    model = User
    template_name = 'form.html'
    form_class = RegistrarUserForm
    success_url = reverse_lazy('login') # pra onde ir depois de cadastrar

    # Como enviar outros dados para tela
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Registrar-se como Aluno'
        context['input'] = 'Enviar'
        return context

class TurmaCreateView(GroupRequiredMixin, LoginRequiredMixin, CreateView): #Tela de crianção de turmas
    group_required = u"representante"
    model = models.Turma
    template_name = 'form.html'
    login_url = '/login/'
    success_url = reverse_lazy('visualizar_turma') # pra onde ir depois de cadastrar
    fields = [
        'nome',
        'alunos',
        #'representante',
        'colegio'
    ]
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Cadastro de Turma'
        context['input'] = 'Cadastrar'
        return context

    # trabalhar com os dados do formulário antes de salvar
    def form_valid(self, form):
        # Definindo o usuário da sessão como representante
        form.instance.representante = self.request.user
        return super().form_valid(form)


class ProfessorCreateView(LoginRequiredMixin, CreateView):  # Cadastro de Professores
    template_name = 'form.html'
    model = models.Professor
    login_url = '/login/'
    success_url = reverse_lazy('visualizar_professor')  # pra onde ir depois de cadastrar
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
    success_url = reverse_lazy('visualizar_colegio')  # pra onde ir depois de cadastrar
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
    success_url = reverse_lazy('visualizar_materia')
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

        context['turmas'] = models.Turma.objects.filter(representante=self.request.user)

        context['titulo'] = 'Cadastro de Materias'
        context['input'] = 'Adicionar Matéria'
        return context


class AtendimentoCreateView(LoginRequiredMixin, CreateView): #Cadastro de atendimentos
    template_name = 'form.html'
    model = models.Atendimento
    login_url = '/login/'
    success_url = reverse_lazy('visualizar_atendimento')
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
    success_url = reverse_lazy('visualizar_aviso')
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


# --------------- UpdateViews --------------- #


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = [
        'first_name',
        'last_name',
        'email',
        # 'is_active'
    ]
    template_name = 'form.html'

    # form_class = RegistrarUserForm
    success_url = reverse_lazy('index') # pra onde ir depois de cadastrar

    # Busca o usuário atual da seção
    def get_object(self, **kwargs):
        object = User.objects.get(pk=self.request.user.pk)
        return object

    # Como enviar outros dados para tela
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Alterar meus dados'
        context['input'] = 'Atualizar'
        return context


#----------------List View---------------#
class UserListView(generic.ListView):
    model = User
    template_name = 'list/user_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Usuarios'
        return context

class ProfessorListView(generic.ListView):
    model = models.Professor
    template_name = 'list/professor_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Professores'
        return context

class ColegioListView(generic.ListView):
    model = models.Colegio
    template_name = 'list/colegio_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Colegios'
        return context


# Esse aqui vai ser para o admin poder alterar alguma coisa sobre a turma
# Quando digo admin, pode ser o admin do django ou o representante
class AdminTurmaListView(generic.ListView):
    model = models.Turma
    template_name = 'list/turma_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Turmas'
        return context

# Esse vai ser um exemplo de lista do ponto de vista do aluno
# Só vamos listar as turmas que o aluno está presente
class TurmaListView(generic.ListView):
    model = models.Turma
    template_name = 'list/turma_list.html'

    # Este é o método para fazer o filtro
    def get_queryset(self):
        # Este é um exemplo de quando só vai trazer a turma que o representante
        # é o usuário que está logado
        # self.object_list = models.Turma.objects.filter(
        #     representante=self.request.user)

        # Quando tem uma relação N para N traz todos as turmas desde que
        # o usuário seja um dos alunos matriculados nela
        self.object_list = models.Turma.objects.filter(
            alunos=self.request.user)
        return self.object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Turmas'
        return context

class MateriaListView(generic.ListView):
    model = models.Materia
    template_name = 'list/materia_list.html'

    def get_context_data(selfself, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Matérias'
        return context

class AtendimentoListView(generic.ListView):
    model = models.Atendimento
    template_name = 'list/atendimento_list.html'

    def get_context_data(selfself, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Atendimentos'
        return context

# Esta vai servir para trazer todos os avisos para o admin/representante
class AdminAvisoListView(generic.ListView):
    model = models.Aviso
    template_name = 'list/aviso_list.html'

    def get_context_data(selfself, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Avisos'
        return context

# Este só vai trazer os avisos das turmas que o usuário logado (aluno) está
class AvisoListView(generic.ListView):
    model = models.Aviso
    template_name = 'list/aviso_list.html'

    # Este é o método para fazer o filtro
    def get_queryset(self):
        # Neste caso vai buscar os avisos somente quando a turma desse aviso
        # tem o usuário logado como um dos alunos, por isso:
        # turma__alunos
        # O __ consegue buscar a relação turmaXaviso
        self.object_list = models.Aviso.objects.filter(
            turma__alunos=self.request.user)

        return self.object_list

    def get_context_data(selfself, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de Avisos'
        return context

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
