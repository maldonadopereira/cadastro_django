from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.br.models import BRPostalCodeField, BRStateField


class Base(models.Model):
    criado = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True

class User(AbstractUser):
    criacao = models.DateTimeField(('Criado em: '), auto_now_add=True)
    atualizacao = models.DateTimeField(('Atualizado em: '), auto_now=True)
    telefone = models.CharField(max_length=15, default='', null=True)
    cep = BRPostalCodeField( null=True)
    endereco = models.CharField(max_length=150, default='', null=True)
    uf = BRStateField(null=True, default='',)
    cidade = models.CharField(max_length=50, default='',  null=True)
    foto_user = models.ImageField(upload_to='fotos/%d/%m/%Y', blank=True, default='')

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.username


class Post(Base):
    titulo = models.CharField('Título', max_length=100)
    conteudo = models.TextField('Conteúdo',max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'

    def __str__(self):
        return self.titulo
