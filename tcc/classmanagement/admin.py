from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Colegio)
admin.site.register(Professor)
admin.site.register(Turma)
admin.site.register(Materia)
admin.site.register(Aviso)
admin.site.register(Atendimento)
