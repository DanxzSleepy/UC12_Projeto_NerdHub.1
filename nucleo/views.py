from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Review, Marca, Carrinho, ItemCarrinho, Pedido
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    produtos = Produto.objects.all()
    marcas = Marca.objects.all() # agora pega todas as marcas tambem 
    return render(request, 'nucleo/index.html', {'produtos': produtos, 'marcas': marcas, 'page_name': 'index'})

def sobre(request):
    return render(request, 'nucleo/sobre.html', {'page_name': 'sobre'})

def suporte(request):
    return render(request, 'nucleo/suporte.html', {'page_name': 'suporte'})

# def detalhe_produto(request, id):
#     produto = get_object_or_404(Produto, id=id)
#     return render(request, 'nucleo/detalhe_produto.html', {
#         'produto': produto,
#         'page_name': 'detalhe_produto'  # Opcional, se quiser usar
#     })

def produtos_por_marca(request, marca_nome):
    marca = Marca.objects.get(nome__iexact=marca_nome)
    produtos = Produto.objects.filter(marca=marca)
    return render(request, 'nucleo/por_marca.html', {'marca': marca, 'produtos': produtos})

# Detalhes e tudo mais Com conta e etc 

def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    relacionados = Produto.objects.filter(marca=produto.marca).exclude(id=produto.id)[:4]
    reviews = produto.reviews.all()
    return render(request, 'nucleo/detalhe_produto.html', {
        'produto': produto,
        'relacionados': relacionados,
        'reviews': reviews
    })


@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if produto.estoque.quantidade < 1:
        messages.error(request, "Produto sem estoque!")
        return redirect('detalhe_produto', produto_id=produto.id)

    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
    item, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
    if not created:
        item.quantidade += 1
    item.save()
    produto.estoque.quantidade -= 1
    produto.estoque.save()
    messages.success(request, "Produto adicionado ao carrinho!")
    return redirect('detalhe_produto', produto_id=produto.id)


@login_required
def adicionar_review(request, produto_id):
    if request.method == "POST":
        produto = get_object_or_404(Produto, id=produto_id)
        texto = request.POST.get("texto")
        nota = int(request.POST.get("nota"))
        Review.objects.create(produto=produto, usuario=request.user, texto=texto, nota=nota)
        messages.success(request, "Review adicionada com sucesso!")
    return redirect('detalhe_produto', produto_id=produto_id)


@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    item, created = ItemCarrinho.objects.get_or_create(
        usuario=request.user,
        produto=produto
    )
    if not created:
        item.quantidade += 1
        item.save()
    return redirect('ver_carrinho')

@login_required
def ver_carrinho(request):
    itens = ItemCarrinho.objects.filter(usuario=request.user)
    total = sum(item.produto.preco * item.quantidade for item in itens)
    return render(request, 'carrinho.html', {'itens': itens, 'total': total})

@login_required
def remover_item_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id, usuario=request.user)
    item.delete()
    return redirect('ver_carrinho')

@login_required
def finalizar_pedido(request):
    itens = ItemCarrinho.objects.filter(usuario=request.user)
    if itens.exists():
        pedido = Pedido.objects.create(usuario=request.user)
        for item in itens:
            pedido.itens.add(item)
        itens.delete()
    return redirect('index')