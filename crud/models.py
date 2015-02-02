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
    email = models.EmailField()
    telefone = models.CharField(max_length=25)

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
    email_professor = models.EmailField()
    telefone_professor = models.CharField(max_length=20)
    monitor = models.CharField(max_length=200)
    email_monitor = models.EmailField()
    telefone_monitor = models.CharField(max_length=20)
    local = models.CharField(max_length=200)
    data_ofertada = models.DateField('data que sera ofertada')
    alunos_matriculados = models.ManyToManyField(Aluno)

    def __unicode__(self):
        """ Retorna o nome da diciplina quando o objeto for pedido """
        return self.nome_diciplina
