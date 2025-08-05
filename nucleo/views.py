from django.shortcuts import render, get_object_or_404
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    return render(request, 'nucleo/index.html', {'produtos': produtos, 'page_name': 'index'})

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
