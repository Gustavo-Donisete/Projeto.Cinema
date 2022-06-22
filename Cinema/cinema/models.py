from django.db import models

# Create your models here.

#Filme, Igresso, Sala, Ator, Sessão
#Subclasse: Tipo de igresso, Categoria Ingresso, Genero Filme
#Ator -> Nome, Papel do Ator

class Tipo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Filme(models.Model):
    nomeFilme = models.CharField(max_length=100)
    duracao = models.IntegerField(null=True)
    genero = models.CharField(max_length=100)

    def __str__(self):
        return self.nomeFilme + '-' + self.genero

class Sala(models.Model):
    numeroSala = models.CharField(max_length=100)
    numeroCadeiras = models.CharField(max_length=100)
    cadeirasDisponiveis = models.CharField(max_length=100)

    def __str__(self):
        return self.numeroSala

class Sessao(models.Model):
    horarios = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True)
    periodo = models.CharField(max_length=100)

    def __str__(self):
        return self.horarios

class Ingresso(models.Model):
    meio = models.CharField(max_length=100)
    inteira = models.CharField(max_length=100)
    fisico = models.CharField(max_length=100)
    online = models.CharField(max_length=100)

    def __str__(self):
        return self.meio + '-' + self.fisico

class Ator (models.Model):
    nome = models.CharField(max_length=100)
    papel = models.CharField(max_length=100)

    def __str__(self):
        return self.nome + '-' + self.papel
