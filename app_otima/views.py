from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from app_otima.models import Fornecedor
from app_otima.forms import FornecedorForm

from app_otima.models import Usuario
from app_otima.forms import UsuarioForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'autenticacao/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required
def home(request):
    return render(request, 'dashboard/home.html', {'title': 'Dashboard'})


@login_required
def fornecedores(request):
    fornecedores = Fornecedor.objects.all()

    return render(request, 'fornecedores/fornecedores.html', {
        'title': 'Fornecedores',
        'fornecedores': fornecedores
    })


@login_required
def adicionar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            novo_fornecedor = form.save()

            messages.success(request, f'Fornecedor "{novo_fornecedor.nome}" adicionado com sucesso!')
            return redirect('fornecedores')
    else:
        form = FornecedorForm()
    return render(request, 'fornecedores/adicionar.html', {
        'title': 'Cadastrar Fornecedor',
        'form': form
    })


@login_required
def editar_fornecedor(request, fornecedor_id):
    return render(request, 'fornecedores/editar.html', {
        'title': f'Editar Fornecedor - Teste',
    })


@login_required
def usuarios(request):
    usuarios = Usuario.objects.all()
    return render (request, 'usuarios/usuarios.html', {
        'title': 'Usuários',
        'usuarios': usuarios
        })

@login_required
def adicionar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            novo_usuario = form.save()

            messages.success(request, f'Usuario "{novo_usuario.nome}" adicionado com sucesso!')
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/adicionar_user.html', {
        'title': 'Cadastrar Usuario',
        'form': form
    })


@login_required
def clientes(request):
    return render(request, 'clientes/clientes.html', {'title': 'Clientes'})


@login_required
def pagamentos(request):
    return render(request, 'pagamentos/pagamentos.html', {'title': 'Pagamentos'})


@login_required
def recebimentos(request):
    return render(request, 'recebimentos/recebimentos.html', {'title': 'Recebimentos'})