from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login as authlogin
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm
from .models import usuario


def index(request):
    if request.user.id:
        mensagem = "Você está Logado."
    else:
        mensagem = "Bem vindo, essa é a página inicial."
    return render(request, 'index.html', {'mensagem': mensagem})

def cadastro_usuario(request):
    form = UsuarioForm()
    if request.POST.get('submit'):
        form = UsuarioForm(request.POST)
        u = usuario()
        u.nome = request.POST.get('nome')
        u.sobrenome = request.POST.get('sobrenome')
        u.email = request.POST.get('email')
        u.senha = request.POST.get('senha')
        u.save()

        if u.id != '':
            mensagem = "Cadastro realizado com sucesso."
            return render(request, 'index.html', {'mensagem': mensagem})
        else:
            return render(request, 'cadastros/cadastro_usuario.html', {'form': form})
    return render(request, 'cadastros/cadastro_usuario.html', {'form': form})

def sobre(request):
    return render(request, 'blocos/sobre.html')

def logar(request):
    form = UsuarioForm()
    return render(request, 'blocos/logar.html', {'form': form})

def validacao(request):
    if request.user.id:
        return render(request, 'index.html')

    if request.POST:
        emailUser = request.POST.get('email')
        senhaUser = request.POST.get('senha')

        u = authenticate(username=emailUser, password=senhaUser)
        if u is not None:
            if u.is_active:
                authlogin(request, u)

                if request.POST.get('next'):
                    return HttpResponseRedirect(request.POST.get('next'))

                return index(request)
    return logar(request)

@login_required
def perfil(request):
    current_user = usuario.objects.get(email = request.user)
    return render(request, 'blocos/perfil.html', {'usuario':current_user})

@login_required
def sair(request):
    logout(request)
    return index(request)
