from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# inserção no banco de dados
from django.contrib.auth import authenticate, login, logout

# Create your views here.

#Pagina inicial
def index(request):
    return render(request, 'index.html')

# Home de usuarios
def home(request):
    return render(request, 'home.html')

#Formulario de cadastro de usuarios
def create(request):
    return render(request, 'create.html')

#Inserção dos dados dos usuarios no banco
def store(request):
    data = {} #data seria um dicionario vazio
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request,'painel.html',data)
    return render(request, 'home.html')

# Formulario do painel de login
def painel(request):
    return render(request, 'painel.html')

# Processa o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/inicial/')
    else:
        data['msg'] = 'Usuário ou senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html',data)

#Pagina inicial
def inicial(request):
    return render(request, 'inicial.html')

# Logout do sistema
def logouts(request):
    logout(request)
    return redirect('/painel/')

# Alterar a senha
def changePassword(request):
    user = User.objects.get(email=request.user.email)
    user.set_password(request.POST['password'])
    user.save()
    logout(request)
    return redirect('/painel/')

# Material
def material(request):
    return render(request, 'material.html')

# rend
def rendimento(request):
    return render(request, 'rendimento.html')

# aulas
def aulas(request):
    return render(request, 'aulas.html')

# hardware
def hardware(request):
    return render(request, 'hardware.html')

# apostila hardware
def aposthdw(request):
    return render(request, 'apostilahardware.html')

# eletrica
def eletrica(request):
    return render(request, 'eletrica.html')

# apostila eletrica
def apostele(request):
    return render(request, 'apostilaeletrica.html')

# automacao
def automacao(request):
    return render(request, 'automacao.html')

# apostila automação
def apostauto(request):
    return render(request, 'apostilaauto.html')

# mecanica
def mecanica(request):
    return render(request, 'mecanica.html')

# apostila mecanica
def apostmec(request):
    return render(request, 'apostilamec.html')

# configuração
def config(request):
    return render(request, 'config.html')