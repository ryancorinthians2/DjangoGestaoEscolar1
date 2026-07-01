from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Curso, Disciplina, Professor, Atribuicao, Aluno

def index(request):
    if request.method == 'POST':
        tipo_usuario = request.POST.get('user_type')
        if tipo_usuario == 'professor': 
            return redirect('professor')
        elif tipo_usuario == 'diretor': 
            return redirect('diretor')
        else: 
            return redirect('aluno')
    return render(request, 'gestao/index.html')

@login_required
def aluno(request):
  
    aluno_atual = Aluno.objects.last()
    
    if aluno_atual:
        nome_aluno = aluno_atual.nome
        curso_nome = aluno_atual.curso.nome
        disciplinas = Disciplina.objects.all()
    else:
        nome_aluno = "Nenhum aluno cadastrado"
        curso_nome = "Nenhum"
        disciplinas = []

    context = {
        'nome_aluno': nome_aluno,
        'curso': curso_nome,
        'disciplinas': disciplinas
    }
    return render(request, 'gestao/aluno.html', context)

@login_required
def professor(request):
    professor_atual = Professor.objects.first()
    
    if professor_atual:
        nome_professor = professor_atual.nome
        atribuicoes = Atribuicao.objects.filter(professor=professor_atual)
        disciplinas = [atrib.disciplina.nome for atrib in atribuicoes]
    else:
        nome_professor = "Nenhum professor cadastrado"
        disciplinas = []

    context = {
        'nome_professor': nome_professor,
        'disciplinas': disciplinas
    }
    return render(request, 'gestao/professor.html', context)

@login_required
def diretor(request):
    if not Professor.objects.exists():
        Professor.objects.create(nome="Mestre Yoda")
        Professor.objects.create(nome="Professor Xavier")
        Professor.objects.create(nome="Girafales")

    if request.method == 'POST':
        qual_botao = request.POST.get('acao')

        if qual_botao == 'cadastrar_curso':
            nome = request.POST.get('nome_curso')
            if nome: 
                Curso.objects.create(nome=nome)

        elif qual_botao == 'cadastrar_disciplina':
            nome = request.POST.get('nome_disciplina')
            if nome: 
                Disciplina.objects.create(nome=nome)

        elif qual_botao == 'cadastrar_professor':
            nome = request.POST.get('nome_professor')
            if nome: 
                Professor.objects.create(nome=nome)

        elif qual_botao == 'atribuir_disciplina':
            disc = request.POST.get('disciplina')
            prof = request.POST.get('professor')
            
            disciplina_obj = Disciplina.objects.filter(nome=disc).first()
            professor_obj = Professor.objects.filter(nome=prof).first()
            
            if disciplina_obj and professor_obj:
                Atribuicao.objects.create(professor=professor_obj, disciplina=disciplina_obj)

        elif qual_botao == 'matricular_aluno':
            aluno_nome = request.POST.get('nome_aluno')
            curso_nome = request.POST.get('curso')
            
            curso_obj = Curso.objects.filter(nome=curso_nome).first()
            
            if aluno_nome and curso_obj:
                Aluno.objects.create(nome=aluno_nome, curso=curso_obj)
            elif qual_botao == 'excluir_curso':
                curso_id = request.POST.get('curso_id')
            if curso_id:
                Curso.objects.filter(id=curso_id).delete()

        
            elif qual_botao == 'excluir_aluno':
                aluno_id = request.POST.get('aluno_id')
                if aluno_id:
                    Aluno.objects.filter(id=aluno_id).delete()

        return redirect('diretor')


    context = {
        'cursos': Curso.objects.all(),
        'disciplinas': Disciplina.objects.all(),
        'professores': Professor.objects.all(),
        'atribuicoes': Atribuicao.objects.all(),
        'matriculas': Aluno.objects.all()
    }
    return render(request, 'gestao/diretor.html', context)