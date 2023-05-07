from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib import messages

from app_otima.models import Fornecedor, Cliente
from app_otima.forms import FornecedorForm, clientesForm

from app_otima.forms import UsuarioForm, EditUsuarioForm

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
    usuarios = User.objects.all()
    return render (request, 'usuarios/usuarios.html', {
        'title': 'Usuários',
        'usuarios': usuarios
    })

@login_required
def adicionar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            dados = form.cleaned_data
            user = form.save(commit=False)
            
            user.set_password(dados['password'])
            user.save()

            messages.success(request, f'Usuario "{user.username}" adicionado com sucesso!')
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/adicionar_user.html', {
        'title': 'Cadastrar Usuario',
        'form': form
    })


@login_required
def editar_usuario(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = EditUsuarioForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Usuario "{user.username}" editado com sucesso!')
            return redirect('usuarios')
    else:
        form = EditUsuarioForm(instance=user)
    return render(request, 'usuarios/adicionar_user.html', {
        'title': f'Editar Usuario: {user.username}',
        'form': form
    })


@login_required
def deletar_usuario(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    user.delete()
    messages.success(request, f'Usuario "{user.username}" deletado com sucesso!')
    return redirect('usuarios')


@login_required
def editar_senha_usuario(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Senha do usuário "{user.username}" alterada com sucesso!')
            return redirect('usuarios')
    else:
        form = SetPasswordForm(user)
    return render(request, 'usuarios/adicionar_user.html', {
        'title': f'Alterar Senha do Usuario: {user.username}',
        'form': form
    })


@login_required
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/clientes.html', {
        'title': 'Cliente',
        'clientes': clientes
                                                      
    })

@login_required
def adicionar_clientes(request):
    if request.method == 'POST':
        form = clientesForm(request.POST)
        if form.is_valid():
            novo_cliente = form.save()

            messages.success(request, f'Cliente "{novo_cliente.nome}" adicionado com sucesso!')
            return redirect('clientes')
    else:
        form = clientesForm()
    return render(request, 'clientes/adicionar_clientes.html', {
        'title': 'Cadastrar Clientes',
        'form': form
    })

@login_required
def pagamentos(request):
    return render(request, 'pagamentos/pagamentos.html', {'title': 'Pagamentos'})


@login_required
def recebimentos(request):
    return render(request, 'recebimentos/recebimentos.html', {'title': 'Recebimentos'})