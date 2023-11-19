from rest_framework.test import APITestCase
from rest_framework import status
from escola.models import Curso
from django.urls import reverse



class CursoTestCase(APITestCase):
    def setUp(self) -> None:
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CTT1', descricao='Curso Teste 1', nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CTT2', descricao='Curso Teste 2', nivel='A'
        )

    # def test_falhador(self):
    #     self.fail('Teste falhou de proposito.')

    def test_requisicao_get_para_listar_cursos(self):
        """Teste para verificar o GET para listar cursos"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_criar_curso(self):
        """Teste para verificar POST para criar cursos"""
        data = {
            'codigo_curso': 'CTT3',
            'descricao': 'Curso Teste 3',
            'nivel': 'A'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_requisicao_delete_para_deletar_curso(self):
        """Teste para verificar DELETE para deletar curso"""
        response = self.client.delete('/cursos/1/')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_curso(self):
        """Teste para verificar PUT para atualizar curso"""
        data = {
            'codigo_curso': 'CTT1',
            'descricao': 'Curso Teste 1 Atualizado',
            'nivel': 'I'
        }
        response = self.client.put('/cursos/1/', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



