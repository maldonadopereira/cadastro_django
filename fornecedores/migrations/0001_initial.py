# Generated by Django 4.0.4 on 2022-04-21 19:31

from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateTimeField(auto_now_add=True, verbose_name='Criado em: ')),
                ('atualizacao', models.DateTimeField(auto_now=True, verbose_name='Atualizado em: ')),
                ('nome', models.CharField(max_length=30)),
                ('cnpj', localflavor.br.models.BRCNPJField(max_length=18)),
                ('cep', localflavor.br.models.BRPostalCodeField(max_length=9, null=True)),
                ('endereco', models.CharField(max_length=150, null=True)),
                ('cidade', models.CharField(max_length=30, null=True)),
                ('uf', models.CharField(max_length=2, null=True)),
                ('telefone', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Fornecedor',
                'verbose_name_plural': 'Fornecedores',
                'ordering': ['-criacao'],
            },
        ),
    ]