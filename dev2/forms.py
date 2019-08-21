from django import forms
from .models import usuario

class UsuarioForm(forms.ModelForm):

    nome = forms.CharField(max_length=78, help_text='Nome:')
    sobrenome = forms.CharField(max_length=128, help_text='Sobrenome:')
    email = forms.CharField(max_length=128, help_text='E-mail:')
    senha = forms.CharField(max_length=128, widget=forms.PasswordInput, help_text='Senha:')

    class Meta:
        model = usuario
        fields = ('nome','sobrenome','email','senha')