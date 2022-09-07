from django.db import models

class Item(models.Model):
	titulo = models.CharField(max_length=150)
	Bio = models.TextField()
	link = models.URLField()
	imagem = models.URLField()
	nome = models.CharField(max_length=140)
	guid = models.CharField(max_length=50, default='None')

	def __str__(self):
		return f'{self.nome}: {self.titulo}'