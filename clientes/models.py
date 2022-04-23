from django.db import models
from localflavor.br.models import *
from core.models import Base


class Cliente(Base):
    nome = models.CharField(max_length=100, null=False)
    telefone = models.CharField(max_length=15, default='')
    cep = BRPostalCodeField()
    endereco = models.CharField(max_length=150, default='')
    cpf = BRCPFField(null=False, unique=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['-criacao']

    def __str__(self):
        return self.nome
    