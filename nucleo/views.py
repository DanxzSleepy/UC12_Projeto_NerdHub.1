from django.shortcuts import render, get_object_or_404
from .models import Produto, Marca


def index(request):
    produtos = Produto.objects.all()
    marcas = Marca.objects.all() # agora pega todas as marcas tambem 
    return render(request, 'nucleo/index.html', {'produtos': produtos, 'marcas': marcas, 'page_name': 'index'})

def sobre(request):
    return render(request, 'nucleo/sobre.html', {'page_name': 'sobre'})

def suporte(request):
    return render(request, 'nucleo/suporte.html', {'page_name': 'suporte'})

def detalhe_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'nucleo/detalhe_produto.html', {
        'produto': produto,
        'page_name': 'detalhe_produto'  # Opcional, se quiser usar
    })

def produtos_por_marca(request, marca_nome):
    marca = Marca.objects.get(nome__iexact=marca_nome)
    produtos = Produto.objects.filter(marca=marca)
    return render(request, 'nucleo/por_marca.html', {'marca': marca, 'produtos': produtos})
