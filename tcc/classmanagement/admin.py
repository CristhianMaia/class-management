from django.contrib import admin

# Register your models here.

# Importa todas as classes do seu models
from .models import *

# Especifica que todas as classes abaixo vão aparecer no menu admin do Django
admin.site.register(Colegio)
admin.site.register(Professor)
admin.site.register(Turma)
admin.site.register(Materia)
admin.site.register(Aviso)
admin.site.register(Atendimento)
