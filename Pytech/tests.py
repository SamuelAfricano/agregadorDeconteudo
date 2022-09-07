from django.test import TestCase

from django.utils import timezone
from .models import Item

class TesteArtigo(TestCase):
	"""Esta class representa os teste de um artigo."""
	def setUp(self):
		self.artigo = Item.objects.create(
			titulo="Um artigo do tech",
			Bio="Uma discricação qualquer",
			link="https://teste.html",
			imagem="https://imagens.html",
			nome="Teste",
			guid="de194720-7b4c-49e2-a05f-432436d3fetr",
		)

	def teste_conteudo_de_artigos(self):
		self.assertEqual(self.artigo.Bio, "Uma discricação qualquer"),
		self.assertEqual(self.artigo.guid, "de194720-7b4c-49e2-a05f-432436d3fetr"),
		self.assertEqual(self.artigo.nome, "Teste")

	def teste_de_roteamento(self):
		resposta = self.client.get("/")
		self.assertEqual(resposta.status_code, 200)