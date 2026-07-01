from django.urls import path
from gestao.views import index, aluno, diretor, professor
urlpatterns = [
    path('', index, name = 'index'),
    path('aluno', aluno, name='aluno'),
    path('diretor', diretor, name='diretor'),
    path('professor',professor, name='professor')
]
