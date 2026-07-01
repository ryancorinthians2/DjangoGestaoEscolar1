from django.contrib import admin
from .models import Curso, Disciplina, Professor, Atribuicao, Aluno

admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Professor)
admin.site.register(Atribuicao)
admin.site.register(Aluno)


