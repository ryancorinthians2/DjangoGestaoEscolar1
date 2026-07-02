from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Curso, Professor

class GestaoEscolarTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='123')
        self.curso = Curso.objects.create(nome="InfoNet")
        self.professor = Professor.objects.create(nome="Mestre Yoda")

    def test_pagina_inicial_carrega_com_sucesso(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


    def test_diretor_bloqueado_para_usuario_anonimo(self):
        response = self.client.get(reverse('diretor'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin/login/', response.url)


    def test_diretor_acessa_com_login(self):
        self.client.login(username='admin', password='123')
        response = self.client.get(reverse('diretor'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mestre Yoda")

    def test_cadastrar_novo_curso_via_diretor(self):
        self.client.login(username='admin', password='123')
        

        dados_formulario = {
            'acao': 'cadastrar_curso', 
            'nome_curso': 'Mecânica'   
        }
        
        response = self.client.post(reverse('diretor'), data=dados_formulario)
        
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Curso.objects.filter(nome='Mecânica').exists())
