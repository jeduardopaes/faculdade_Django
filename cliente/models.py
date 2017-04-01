from __future__ import unicode_literals

from django.db import models

'''
class Questions(models.Model):
    question_text = models.CharField( max_length=250 )
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey('Questions', on_delete=models.CASCADE)
    choice_text = models.CharField( max_length=250 )
    votes = models.IntegerField(default=0)
'''
# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    cep = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15, unique=True)
    

