from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Perfil, Endereco

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
            # Update last login time
            if hasattr(user, 'perfil'):
                user.perfil.last_login_at = timezone.now()
                user.perfil.save()
            
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

@login_required
def perfil(request):
    """
    View para exibir e editar o perfil do usuário
    """
    # Get or create profile for users who don't have one
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        # Atualizar informações básicas
        perfil.display_name = request.POST.get('display_name', perfil.display_name)
        perfil.first_name = request.POST.get('first_name', perfil.first_name)
        perfil.last_name = request.POST.get('last_name', perfil.last_name)
        perfil.bio = request.POST.get('bio', perfil.bio)
        perfil.phone = request.POST.get('phone', perfil.phone)
        
        # Atualizar preferências
        perfil.newsletter_subscribed = request.POST.get('newsletter_subscribed') == 'on'
        perfil.marketing_opt_in = request.POST.get('marketing_opt_in') == 'on'
        
        perfil.save()
        messages.success(request, "Perfil atualizado com sucesso!")
        return redirect('usuario:perfil')
    
    return render(request, 'usuarios/perfil.html', {'perfil': perfil})

@login_required
def enderecos(request):
    """
    View para gerenciar endereços do usuário
    """
    # Get or create profile for users who don't have one
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    enderecos = perfil.enderecos.all()
    
    if request.method == "POST":
        # Adicionar novo endereço
        label = request.POST.get('label')
        recipient_name = request.POST.get('recipient_name')
        street = request.POST.get('street')
        number = request.POST.get('number')
        complement = request.POST.get('complement', '')
        neighborhood = request.POST.get('neighborhood')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal_code')
        phone_at_address = request.POST.get('phone_at_address', '')
        
        Endereco.objects.create(
            perfil=perfil,
            label=label,
            recipient_name=recipient_name,
            street=street,
            number=number,
            complement=complement,
            neighborhood=neighborhood,
            city=city,
            state=state,
            postal_code=postal_code,
            phone_at_address=phone_at_address
        )
        
        messages.success(request, "Endereço adicionado com sucesso!")
        return redirect('usuario:enderecos')
    
    return render(request, 'usuarios/enderecos.html', {'enderecos': enderecos})

@login_required
def endereco_editar(request, endereco_id):
    """
    View para editar um endereço específico
    """
    # Get or create profile for users who don't have one
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    endereco = get_object_or_404(Endereco, id=endereco_id, perfil=perfil)
    
    if request.method == "POST":
        endereco.label = request.POST.get('label', endereco.label)
        endereco.recipient_name = request.POST.get('recipient_name', endereco.recipient_name)
        endereco.street = request.POST.get('street', endereco.street)
        endereco.number = request.POST.get('number', endereco.number)
        endereco.complement = request.POST.get('complement', endereco.complement)
        endereco.neighborhood = request.POST.get('neighborhood', endereco.neighborhood)
        endereco.city = request.POST.get('city', endereco.city)
        endereco.state = request.POST.get('state', endereco.state)
        endereco.postal_code = request.POST.get('postal_code', endereco.postal_code)
        endereco.phone_at_address = request.POST.get('phone_at_address', endereco.phone_at_address)
        
        endereco.save()
        messages.success(request, "Endereço atualizado com sucesso!")
        return redirect('usuario:enderecos')
    
    return render(request, 'usuarios/endereco_editar.html', {'endereco': endereco})

@login_required
def endereco_excluir(request, endereco_id):
    """
    View para excluir um endereço
    """
    # Get or create profile for users who don't have one
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    endereco = get_object_or_404(Endereco, id=endereco_id, perfil=perfil)
    endereco.delete()
    messages.success(request, "Endereço excluído com sucesso!")
    return redirect('usuario:enderecos')