from django.db import models

# Create your models here.
class Base(models.Model):
    criacao = models.DateTimeField(('Criado em: '), auto_now_add=True)
    atualizacao = models.DateTimeField(('Atualizado em: '), auto_now=True)

    class Meta:
        abstract = True
