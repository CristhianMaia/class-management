from django.db import models
#created_at = models.DateTimeField(auto_now_add=True)
#updated_at = models.DateTimeField(auto_now=True)
#horarios: CharField:length=5
from django.contrib.auth.models import User

class Colegio(models.Model):
    nome                    = models.CharField(max_length=240, blank= False, null=False, help_text='Obrigatório.')
    data_cadastro           = models.DateField(auto_now_add=True)

    # Método que vai retornar o nome do objeto quando for imprimir um objeto, como se fosse um toString
    def __str__(self):
        return self.nome

    # Define como será chamada essa classe nas telas porque o nome tema acento
    # Só é necessário se a palavra tem acentos
    class Meta:
        verbose_name = 'Colégio'
        verbose_name_plural = 'Colégios'


class Professor(models.Model):
    nome                    = models.CharField(max_length=120, blank=False, null=False, help_text='Obrigatório.')
    email                   = models.EmailField(max_length=120, blank=False, null=False, help_text='Obrigatório.')

    # Método que vai retornar o nome do objeto quando for imprimir um objeto, como se fosse um toString
    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome                    = models.CharField(max_length=120, blank=False, null=False, help_text='Obrigatório.')
    alunos                  = models.ManyToManyField(User, help_text='Obrigatório', related_name='alunos_matriculados')
    data_cadastro           = models.DateField(auto_now_add=True)
    representante           = models.ForeignKey(User, on_delete=models.PROTECT, blank=False, null=False)
    colegio                 = models.ForeignKey(Colegio, on_delete=models.PROTECT, blank=False, null=False, help_text='Obrigatório.')

    # Método que vai retornar o nome do objeto quando for imprimir um objeto, como se fosse um toString
    def __str__(self):
        return self.nome


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
    nome                    = models.CharField(max_length=120, blank=False, null=False, help_text='Obrigatório.')
    local                   = models.CharField(max_length=120, blank=False, null=False, help_text='Obrigatório.')
    dia                     = models.CharField(max_length=3, blank=False, null=False, choices=DIA_CHOICES, help_text='Obrigatório.')
    horario_inicio          = models.CharField(max_length=5, blank=False, null=False)
    horario_fim             = models.CharField(max_length=5, blank=False, null=False)
    turma                   = models.ForeignKey(Turma, on_delete=models.PROTECT, null=False, blank=False)
    professor               = models.ForeignKey(Professor, on_delete=models.PROTECT, null=False, blank=False)

    # Método que vai retornar o nome do objeto quando for imprimir um objeto, como se fosse um toString
    def __str__(self):
        return self.nome

    # Define como será chamada essa classe nas telas porque o nome tema acento
    # Só é necessário se a palavra tem acentos
    class Meta:
        verbose_name = 'Matéria'
        verbose_name_plural = 'Matérias'

class Avisos(models.Model):
    AVISO_CHOICES   = (
        ('N', 'Aviso'), #Notice
        ('H', 'Tarefa'), #Homework
        ('W', 'Trabalho'), #Work
        ('E', 'Prova'), #Exam
    )
    data_final              = models.DateField(auto_now=False, auto_now_add=False, blank=False, null=False)
    tipo_aviso              = models.CharField(max_length=1, choices=AVISO_CHOICES, null=False, blank=False, help_text='Obrigatório.')
    comentarios             = models.TextField(null=True, blank=True)
    ultima_modificacao      = models.DateField(auto_now=True)
    data_post               = models.DateField(auto_now_add=True)
    turma                   = models.ForeignKey(Turma, on_delete=models.PROTECT, null=False, blank=False)
    materia                 = models.ForeignKey(Materia, on_delete=models.PROTECT, null=False, blank=False)

    # Método que vai retornar o nome do objeto quando for imprimir um objeto, como se fosse um toString
    def __str__(self):
        return self.nome


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
    turma                   = models.ForeignKey(Turma, on_delete=models.PROTECT, blank=False, null=False, help_text='Obrigatório.')
    professor               = models.ForeignKey(Professor, on_delete=models.PROTECT, blank=False, null=False, help_text='Obrigatório.')
    dia                     = models.CharField(max_length=3, choices=DIA_CHOICES, blank=False, null=False, help_text='Obrigatório.')
    horario_inicio          = models.CharField(max_length=5, blank=False, null=False, help_text='Obrigatório.')
    horario_fim             = models.CharField(max_length=5, blank=False, null=False, help_text='Obrigatório.')

    # Método que vai retornar o nome do objeto quando for imprimir um objeto, como se fosse um toString
    def __str__(self):
        return self.nome
