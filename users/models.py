from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.br.models import BRPostalCodeField, BRStateField


class User(AbstractUser):
    criacao = models.DateTimeField(('Criado em: '), auto_now_add=True)
    atualizacao = models.DateTimeField(('Atualizado em: '), auto_now=True)
    telefone = models.CharField(max_length=15, default='', null=True)
    cep = BRPostalCodeField( null=True)
    endereco = models.CharField(max_length=150, default='', null=True)
    uf = BRStateField(null=True, default='',)
    cidade = models.CharField(max_length=50, default='',  null=True)
    foto_user = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True, default='')
