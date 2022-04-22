from django.db import models
from fornecedores.models import Fornecedor
from django.contrib.auth.models import User

class Base(models.Model):
    criacao = models.DateTimeField(('Criado em: '), auto_now_add=True)
    atualizacao = models.DateTimeField(('Atualizado em: '), auto_now=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField(max_length=30, null=False )
    marca = models.CharField(max_length=50, null=True)
    preco = models.FloatField(null=False)
    quantidade = models.IntegerField(default=0)
    descricao = models.TextField(max_length=500)
    disponivel = models.BooleanField(default=False)
    user = models.ForeignKey(User, default='', on_delete=models.CASCADE, null=True)
    fornecedor = models.ForeignKey(Fornecedor, default='', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['-criacao']

    def __str__(self):
        return self.nome