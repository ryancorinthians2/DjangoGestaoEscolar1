from django.db import models

class Curso(models.Model):
    nome= models.CharField(max_length=100)

    def __str__(self):
        return self.nome 
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Professor(models.Model):
    nome = models.CharField(max_length = 100)
    
class Atribuicao(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.professor.nome} -> {self.disciplina.nome}"

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.curso.nome})"
    

