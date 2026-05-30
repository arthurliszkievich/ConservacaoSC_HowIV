from django import forms
from .models import UnidadeConservacao, Comunicacao, Instituicao, Municipio


class UnidadeConservacaoForm(forms.ModelForm):
    """Formulário para criar e editar UC"""
    class Meta:
        model = UnidadeConservacao
        fields = ['nome', 'descricao', 'instituicao', 'municipios', 'imagem', 'data_criacao', 'area']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'instituicao': forms.Select(attrs={'class': 'form-control'}),
            'municipios': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'data_criacao': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 6.667 hectares'}),
        }

class ComunicacaoForm(forms.ModelForm):
    """Formulário para enviar uma comunicação sobre uma Unidade."""
    class Meta:
        model = Comunicacao
        fields = ['titulo', 'descricao', 'email']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class InstituicaoForm(forms.ModelForm):
    """Formulário para criar uma nova Instituição."""
    class Meta:
        model = Instituicao
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: IMA, ICMBio...'}),
        }

class MunicipioForm(forms.ModelForm):
    """Formulário para criar um novo Município."""
    class Meta:
        model = Municipio
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Florianópolis'}),
        }

