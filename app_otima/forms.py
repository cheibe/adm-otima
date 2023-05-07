from django import forms
from app_otima.models import Fornecedor

from app_otima.models import Usuario

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
        model = Usuario
        fields = [
            'nome', 
            'email',
            'senha'
        ]