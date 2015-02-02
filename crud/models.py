""" descricao das tabelas do banco """
from django.db import models

# Create your models here.


class Aluno(models.Model):
    """ Aluno eh a tabela que contera os alunos matriculados no sitema
        nome_aluno: string contendo nome do aluno
        data_nascimento: contem a data de nascimento do aluno
    """
    nome_aluno = models.CharField(max_length=200)
    data_nascimento = models.DateField('data de nascimento')

    def __unicode__(self):
        """ Retorna o nome do aluno quando pedirmos o objeto """
        return self.nome_aluno


class Turma(models.Model):
    """ Turma base de dados das turmas cadastradas
        nome_diciplina: nome da diciplina ofertada
        professor: professor que ofertou a diciplina
        monitor: monitor da diciplina overtada
        data_ofertada: data em que foi ofertada a diciplina
        alunos_matriculados: relacionamento com alunos
    """
    nome_diciplina = models.CharField(max_length=200)
    professor = models.CharField(max_length=200)
    monitor = models.CharField(max_length=200)
    data_ofertada = models.DateField('data que sera ofertada')
    alunos_matriculados = Aluno()

    def __unicode__(self):
        """ Retorna o nome da diciplina quando o objeto for pedido """
        return self.nome_diciplina


class Usuario(models.Model):
    """ Usuario eh a base de dados dos usuario do sistema
    """
    nome = models.CharField(max_length=200)
    login = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)

    def __unicode__(self):
        """ Retorna nome quando pedirmos o objeto """
        return self.nome
