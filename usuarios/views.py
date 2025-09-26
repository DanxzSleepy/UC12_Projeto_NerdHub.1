from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def conta(request):
    if request.method == "GET":
        # If user is already authenticated, redirect to index
        if hasattr(request, 'user') and request.user.is_authenticated:
            # Check if there's a next parameter
            next_url = request.GET.get('next', 'nucleo:index')
            if next_url == 'nucleo:index' or not next_url:
                return redirect('nucleo:index')
            else:
                return redirect(next_url)
        return render(request, 'usuarios/conta.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        
        if user:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            # Check if there's a next parameter
            next_url = request.GET.get('next', 'nucleo:index')
            if next_url and ('conta' in str(next_url) or 'cadastro' in str(next_url)):
                next_url = 'nucleo:index'
            return redirect(next_url)
        else:
            messages.error(request, "Usuário ou senha inválidos!")
            return render(request, 'usuarios/conta.html')

def cadastro(request):
    if request.method == "GET":
        # If user is already authenticated, redirect to index
        if hasattr(request, 'user') and request.user.is_authenticated:
            return redirect('nucleo:index')
        return render(request, 'usuarios/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        # Verificar se usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, "Já existe um usuário com este nome!")
            return render(request, 'usuarios/cadastro.html')
        
        # Verificar se email já existe
        if User.objects.filter(email=email).exists():
            messages.error(request, "Já existe um usuário com este email!")
            return render(request, 'usuarios/cadastro.html')
        
        # Criar usuário
        user = User.objects.create_user(username=username, email=email, password=senha)
        messages.success(request, "Usuário cadastrado com sucesso!")
        login(request, user)
        return redirect('nucleo:index')
        
def user_logout(request):
    logout(request)
    messages.success(request, "Você saiu da sua conta!")
    return redirect('nucleo:index')