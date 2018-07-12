"""classmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.conf.urls import include


urlpatterns = [
    path('', views.Index.as_view(), name="index"),

    path('turmas/', views.TurmasTemplateView.as_view(), name='turmas'),  # Tela das turmas disponiveis para o usuario
    #path('login/', views.Login.as_view(), name='login'),

#-------Cadastros------#
    path('registrar/', views.UserCreateView.as_view(), name='cadastrar_user'),
    path('cadastrar/professor/', views.ProfessorCreateView.as_view(), name='cadastrar_professor'),
    path('cadastrar/colegio/', views.ColegioCreateView.as_view(), name='cadastrar_colegio'),
    path('cadastrar/turma/', views.TurmaCreateView.as_view(), name='cadastrar_turma'),   # tela para criar novas turmas por meio de um botao da tela Turmas
    path('cadastrar/materia/', views.MateriaCreateView.as_view(), name='cadastrar_materia'),
    path('cadastrar/atendimento/', views.AtendimentoCreateView.as_view(), name='cadastrar_atendimento'),
    path('cadastrar/aviso/', views.AvisoCreateView.as_view(), name='cadastrar_aviso'),

#--------Atualizar Cadastros--------#
    path('meus-dados/', views.UserUpdateView.as_view(), name='meus-dados'),

    path('atualizar/', views.UserUpdateView.as_view(), name='atualizar_user'),
    path('atualizar/professor/<pk>', views.ProfessorUpdateView.as_view(), name='atualizar_professor'),
    path('atualizar/turma/<pk>', views.TurmaUpdateView.as_view(), name='atualizar_turma'),
    path('atualizar/colegio/<pk>', views.ColegioUpdateView.as_view(), name='atualizar_colegio'),
    path('atualizar/materia/<pk>', views.MateriaUpdateView.as_view(), name='atualizar_materia'),
    path('atualizar/atendimento/<pk>', views.AtendimentoUpdateView.as_view(), name='atualizar_atendimento'),
    path('atualizar/aviso/<pk>', views.AvisoUpdateView.as_view(), name='atualizar_aviso'),

#-------Deletar Cadastros----------#
    path('deletar/professor/<pk>', views.ProfessorDeleteView.as_view(), name='deletar_professor'),
    path('deletar/turma/<pk>', views.TurmaDeleteView.as_view(), name='deletar_turma'),
    path('deletar/colegio/<pk>', views.ColegioDeleteView.as_view(), name='deletar_colegio'),
    path('deletar/materia/<pk>', views.MateriaDeleteView.as_view(), name='deletar_materia'),
    path('deletar/atendimento/<pk>', views.AtendimentoDeleteView.as_view(), name='deletar_atendimento'),
    path('deletar/aviso/<pk>', views.AvisoDeleteView.as_view(), name='deletar_aviso'),

#--------Listas--------#
    path('visualizar/alunos', views.UserListView.as_view(), name='visualizar_usuarios'),
    path('visualizar/professor', views.ProfessorListView.as_view(), name='visualizar_professor'),
    path('visualizar/colegio/', views.ColegioListView.as_view(), name='visualizar_colegio'),
    path('visualizar/turma/', views.TurmaListView.as_view(), name='visualizar_turma'),
    path('visualizar/materia/', views.MateriaListView.as_view(), name='visualizar_materia'),
    path('visualizar/atendimento/', views.AtendimentoListView.as_view(), name='visualizar_atendimento'),
    path('visualizar/aviso/', views.AvisoListView.as_view(), name='visualizar_aviso'),

#------Telas--------#
    path('turma/1/', views.TurmaTemplateView.as_view(), name='turmaID'),   # Turma selecionada pelo usuario por meio da tela Turmas
    path('turma/1/info/', views.InfoTurma.as_view(), name='info_turma'),     # info da turma em que estava selecionada por meio de botao na tela Turma
    path('turma/1/horarios/', views.HorariosTemplateView.as_view(), name='horarios aula'),
    path('turma/1/atendimentos/', views.AtendimentosTemplateView.as_view(), name='atendimentos'),

    path('turma/1/adicionar_aviso/', views.AvisoCreateView.as_view(), name='cadastrar aviso'),
    path('turma/1/adicionar_aluno/', views.AlunosCreateView.as_view(), name='cadastrar aluno'),

#------Autenticação-----#

#----- Proteção exclusão ---#
    #path('erro/exclusao/', TemplateView.as_view(template_name="protectDelete.html"), name='protectDelete'),
]
