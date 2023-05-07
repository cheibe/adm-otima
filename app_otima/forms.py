from django import forms
from app_otima.models import Fornecedor, Cliente

from django.contrib.auth.models import User

class FornecedorForm(forms.ModelForm):
    
    class Meta:
        model = Fornecedor
        fields = [
            'nome', 
            'telefone', 
            'documento', 
            'rua', 
            'numero', 
            'bairro', 
            'cidade', 
            'estado'
        ]


class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'is_superuser',
            'first_name',
            'last_name',
            'is_staff',
            'is_active'
        ]
        widgets = {
            'password': forms.widgets.PasswordInput
        }


class EditUsuarioForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'is_superuser',
            'first_name',
            'last_name',
            'is_staff',
            'is_active'
        ]


class clientesForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = [
            'nome', 
            'telefone', 
            'documento', 
            'rua', 
            'numero', 
            'bairro', 
            'cidade', 
            'estado'
        ]