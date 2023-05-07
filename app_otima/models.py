from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=120, verbose_name='Nome')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    documento = models.CharField(max_length=20, verbose_name='CPF/CNPJ')
    rua = models.CharField(max_length=250, verbose_name='Logradouro')
    numero = models.CharField(max_length=10, verbose_name='Número')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    estado = models.CharField(max_length=2, verbose_name='Estado')


class Usuario(models.Model):
    nome = models.CharField(max_length=120, verbose_name='Nome')
    email = models.CharField(max_length=50, verbose_name='email')
    senha = models.CharField(max_length=20, verbose_name='senha')