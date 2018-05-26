from django.views.generic import TemplateView

#Telas iniciais


class Index(TemplateView):
    template_name = 'index_base.html'

class Sobre(TemplateView):
    template_name = 'sobre.html'


#Telas iniciais pos-login
class Turmas(TemplateView): #Tela de turmas do usuario - pos login
    template_name = 'turmas.html'
    login_url = '/entrar/'

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

