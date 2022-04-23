from django.db import models
from localflavor.br.models import *
from core.models import Base


class Fornecedor(Base):
    nome = models.CharField(max_length=30)
    cnpj = BRCNPJField()
    cep = BRPostalCodeField(null=True)
    endereco = models.CharField(max_length=150, null=True)
    cidade = models.CharField(max_length=30, null=True)
    uf = models.CharField(max_length=2, null=True)
    telefone= models.CharField(max_length=15, null=True)
    email = models.EmailField(max_length=50, null=True)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering = ['-criacao']

    def __str__(self):
        return self.nome

