from django.db import models
from datetime import datetime

# Create your models here.
class Usuario(models.Model):
	FUNCAO = {
		('O','Operador'),
		('A','Administrador')
	}
	nome = models.CharField(max_length=50, null=False)
	nome_usuario = models.CharField(max_length=25, null=False)
	funcao = models.CharField(max_length=1, choices=FUNCAO)
	status = models.BooleanField(default=True)

	def __str__(self):
		return self.nome

class Questao(models.Model):
	enunciado = models.TextField(null=False)

	def __str__(self):
		return self.enunciado

class Avaliacao(models.Model):
	periodo_inicio = models.DateTimeField(null=False)
	periodo_fim = models.DateTimeField(null=False)
	criado_em = models.DateTimeField(auto_now_add = True)
	questoes = models.ManyToManyField(Questao)

	def __str__(self):
		return 'De: ' + '{:%m/%d/%Y}'.format(self.periodo_inicio) + ' a ' + '{:%m/%d/%Y}'.format(self.periodo_fim)

class Resposta(models.Model):
	valor = models.IntegerField(null=False)
	criado_em = models.DateTimeField(auto_now_add=True)
	atualizado_em = models.DateTimeField(auto_now_add=True)
	usuario = models.ForeignKey(Usuario, on_delete = models.CASCADE, related_name = 'usuarios')
	avaliacao = models.ForeignKey(Avaliacao, on_delete = models.CASCADE, related_name= 'avaliacoes')
	questao = models.ForeignKey(Questao, on_delete= models.CASCADE, related_name = "questoes")
	criado_em = models.DateTimeField(auto_now_add = True)

	#def __str__(self):
		# return 'Usuario: ' + self.usuario + ', Avaliacao: ' + self.avaliacao + ', Resposta: ' + self.valor
		#return self.valor