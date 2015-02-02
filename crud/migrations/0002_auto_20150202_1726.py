# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='aluno',
            name='email',
            field=models.EmailField(default='vazio', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aluno',
            name='telefone',
            field=models.CharField(default='vazio', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turma',
            name='alunos_matriculados',
            field=models.ManyToManyField(to='crud.Aluno'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='turma',
            name='email_monitor',
            field=models.EmailField(default='vazio', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turma',
            name='email_professor',
            field=models.EmailField(default='vazio', max_length=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turma',
            name='local',
            field=models.CharField(default='vazio', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turma',
            name='telefone_monitor',
            field=models.CharField(default='vazio', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='turma',
            name='telefone_professor',
            field=models.CharField(default='vazio', max_length=20),
            preserve_default=False,
        ),
    ]
