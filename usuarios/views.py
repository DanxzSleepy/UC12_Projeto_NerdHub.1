from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def conta(request:HttpRequest):
    if request.method == "GET":
        return render(request, 'usuarios/conta.html')
    
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        
        if user:
            login(request, user)
            return render(request, 'usuarios/autenticado.html')
        
        else:
            return HttpResponse("Usuario ou senha inválidos")
        

def cadastro(request:HttpRequest):
    if request.method == "GET":
        return render(request, 'usuarios/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse("Já existe um usuário com este nome!")
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        
        return HttpResponse("Usuário cadastrado com sucecesso!" )
     
    

        
    