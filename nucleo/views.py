from django.shortcuts import render, get_object_or_404
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    return render(request, 'nucleo/index.html', {'produtos': produtos})

def detalhe_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    return render(request, 'nucleo/detalhe_produto.html', {'produto': produto})