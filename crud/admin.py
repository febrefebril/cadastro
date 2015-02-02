""" configura pagina de administrador do django """
# -*- coding: utf-8 -*-
from django.contrib import admin
from crud.models import Aluno, Turma
# Register your models here.


class QuestionAdmin(admin.ModelAdmin):
    """ Ordena como sera mostrado os formularios da pagina do admin """
    fieldsets = [('Responsáveis pela diciplina',
                 {'fields': ['professor', 'monitor']}),
                 ('Informações gerais',
                 {'fields': ['nome_diciplina', 'data_ofertada']}), ]

admin.site.register(Aluno)
admin.site.register(Turma, QuestionAdmin)
