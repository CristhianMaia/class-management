from django.db import models
#created_at = models.DateTimeField(auto_now_add=True)
#updated_at = models.DateTimeField(auto_now=True)
#horarios: CharField:length=5
from django.contrib.auth.models import User
class Colegio(models.Model):
    nome                    = models.CharField(max_length=240, blank= False, null=False, help_text='Obrigatório.')
    data_cadastro           = models.DateField(auto_now_add=True)

class Professor(models.Model):
    nome                    = models.CharField(max_length=120, blank=False, null=False, help_text='Obrigatório.')
    email                   = models.EmailField(max_length=120, blank=False, null=False, help_text='Obrigatório.')

class Turma(models.Model):
    nome                    = models.CharField(max_length=120, blank=False, null=False, help_text='Obrigatório.')
    alunos                  = models.ManyToManyField(User, on_delete=models.CASCADE, null=False)
    data_cadastro           = models.DateField(auto_now_add=True)
    representante           = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    colegio                 = models.ForeignKey(Colegio, null=False, blank=False, help_text='Obrigatório.')


class Materia(models.Model):
    DIA_CHOICES   = (
        ('Seg', 'Segunda'),
        ('Ter', 'Terca'),
        ('Qua', 'Quarta'),
        ('Qui', 'Quinta'),
        ('Sex', 'Sexta'),
        ('Sab', 'Sabado'),
        ('Dom', 'Domingo'),
    )
    nome                    = models.CharField(max_length=120, help_text='Obrigatório.')
    local                   = models.CharField(max_length=120, help_text='Obrigatório.')
    dia                     = models.CharField(max_length=3, choices=DIA_CHOICES, help_text='Obrigatório.')
    horario_inicio          = models.CharField(max_length=5, blank=False, null=False)
    horario_fim             = models.CharField(max_length=5, blank=False, null=False)
    turma                   = models.ForeignKey(Turma, null=False, blank=False)
    professor               = models.ForeignKey(Professor, null=False, blank=False)

class Avisos(models.Model):
    AVISO_CHOICES   = (
        ('N', 'Aviso'), #Notice
        ('H', 'Tarefa'), #Homework
        ('W', 'Trabalho'), #Work
        ('E', 'Prova'), #Exam
    )
    data_final              = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=False)
    tipo_aviso              = models.CharField(max_length=1, choices=AVISO_CHOICES, help_text='Obrigatório.')
    comentarios             = models.TextField(null=True, blank=True)
    ultima_modificacao      = models.DateField(auto_now=True)
    data_post               = models.DateField(auto_now_add=True)
    turma                   = models.ForeignKey(Turma, null=False, blank=False)
    materia                 = models.ForeignKey(Materia, null=False, blank=False)

class Atendimento(models.Model):
    DIA_CHOICES   = (
        ('Seg', 'Segunda'),
        ('Ter', 'Terca'),
        ('Qua', 'Quarta'),
        ('Qui', 'Quinta'),
        ('Sex', 'Sexta'),
        ('Sab', 'Sabado'),
        ('Dom', 'Domingo'),
    )
    turma                   = models.ForeignKey(Turma, null=False)
    professor               = models.ForeignKey(Professor, null=False)
    dia                     = models.CharField(max_length=3, choices=DIA_CHOICES, blank=False, null=False, help_text='Obrigatório.')
    horario_inicio          = models.CharField(max_length=5, blank=False, null=False)
    horario_fim             = models.CharField(max_length=5, blank=False, null=False)
