# Generated by Django 4.0.4 on 2022-04-22 22:28

from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em: ')),
                ('atualizacao', models.DateTimeField(auto_now=True, verbose_name='Atualizado em: ')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(default='', max_length=15)),
                ('cep', localflavor.br.models.BRPostalCodeField(max_length=9)),
                ('endereco', models.CharField(default='', max_length=150)),
                ('cpf', localflavor.br.models.BRCPFField(max_length=14, unique=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['-criacao'],
            },
        ),
    ]
