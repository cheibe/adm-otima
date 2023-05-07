# Generated by Django 4.2 on 2023-05-07 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_otima', '0002_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('documento', models.CharField(max_length=20, verbose_name='CPF/CNPJ')),
                ('rua', models.CharField(max_length=250, verbose_name='Logradouro')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
            ],
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]