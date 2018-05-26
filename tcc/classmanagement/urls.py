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
from . import views


urlpatterns = [
    path(r'', views.Index.as_view(), name="index"),
    path('sobre/', views.Sobre.as_view(), name="sobre"),

    path('turmas/', views.Turmas.as_view(), name='turmas'),  # Tela das turmas disponiveis para o usuario
    path('criarturma/', views.CriacaoTurma.as_view(), name='criação de turma'),
    # tela para criar novas turmas por meio de um botao da tela Turmas

    path('turmas/turmaID/', views.Turma.as_view(), name='turma'),
    # Turma selecionada pelo usuario por meio da tela Turmas
    path('turmas/turmaID/info/', views.InfoTurma.as_view(), name='info_turma'),
    # info da turma em que estava selecionada por meio de botao na tela Turma
]
