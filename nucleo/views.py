from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Review, Marca, Carrinho, ItemCarrinho, Pedido, Estoque, ItemPedido
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    produtos = Produto.objects.all()
    marcas = Marca.objects.all()
    return render(request, 'nucleo/index.html', {'produtos': produtos, 'marcas': marcas, 'page_name': 'index'})

def sobre(request):
    return render(request, 'nucleo/sobre.html', {'page_name': 'sobre'})

def suporte(request):
    return render(request, 'nucleo/suporte.html', {'page_name': 'suporte'})

def produtos_por_marca(request, marca_nome):
    marca = get_object_or_404(Marca, nome__iexact=marca_nome)
    produtos = Produto.objects.filter(marca=marca)
    return render(request, 'nucleo/por_marca.html', {'marca': marca, 'produtos': produtos})

def detalhe_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    relacionados = Produto.objects.filter(marca=produto.marca).exclude(id=produto.id)[:4]
    reviews = Review.objects.filter(produto=produto)
    return render(request, 'nucleo/detalhe_produto.html', {
        'produto': produto,
        'relacionados': relacionados,
        'reviews': reviews
    })


@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    # Verificar se o produto tem estoque
    try:
        estoque = produto.estoque
        if estoque.quantidade < 1:
            messages.error(request, "Produto sem estoque!")
            return redirect('nucleo:detalhe_produto', produto_id=produto.id)
    except:
        messages.error(request, "Produto sem estoque cadastrado!")
        return redirect('nucleo:detalhe_produto', produto_id=produto.id)

    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
    item, created = ItemCarrinho.objects.get_or_create(carrinho=carrinho, produto=produto)
    
    if not created:
        # Verificar se há estoque suficiente antes de incrementar
        if estoque.quantidade > item.quantidade:
            item.quantidade += 1
            item.save()
            messages.success(request, "Quantidade atualizada no carrinho!")
        else:
            messages.error(request, "Quantidade indisponível em estoque!")
    else:
        item.quantidade = 1
        item.save()
        messages.success(request, "Produto adicionado ao carrinho!")
    
    return redirect('nucleo:detalhe_produto', produto_id=produto.id)


@login_required
def adicionar_review(request, produto_id):
    if request.method == "POST":
        produto = get_object_or_404(Produto, id=produto_id)
        texto = request.POST.get("texto")
        nota = request.POST.get("nota")
        if nota:
            nota = int(nota)
        else:
            nota = 5
        Review.objects.create(
            produto=produto, 
            usuario=request.user, 
            comentario=texto, 
            nota=nota
        )
        messages.success(request, "Review adicionada com sucesso!")
    return redirect('nucleo:detalhe_produto', produto_id=produto_id)


@login_required
def ver_carrinho(request):
    # Obter ou criar carrinho para o usuário
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
    itens = carrinho.itens.all()
    
    # Calcular o total para cada item
    itens_com_total = []
    total_geral = 0
    
    for item in itens:
        total_item = item.produto.preco * item.quantidade
        total_geral += total_item
        itens_com_total.append({
            'item': item,
            'total': total_item
        })
    
    return render(request, 'nucleo/carrinho.html', {
        'itens_com_total': itens_com_total,
        'total': total_geral
    })

@login_required
def remover_item_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    # Verificar se o item pertence ao carrinho do usuário
    if item.carrinho.usuario == request.user:
        item.delete()
        messages.success(request, "Item removido do carrinho!")
    else:
        messages.error(request, "Você não tem permissão para remover este item!")
    return redirect('nucleo:ver_carrinho')

@login_required
def finalizar_pedido(request):
    carrinho, created = Carrinho.objects.get_or_create(usuario=request.user)
    itens = carrinho.itens.all()
    
    if itens.exists():
        # Criar o pedido
        pedido = Pedido.objects.create(usuario=request.user)
        
        # Adicionar itens ao pedido
        for item in itens:
            # Atualizar a quantidade no estoque
            try:
                estoque = item.produto.estoque
                estoque.quantidade -= item.quantidade
                estoque.save()
            except:
                pass  # Produto sem estoque controlado
            
            # Criar o item do pedido
            ItemPedido.objects.create(
                pedido=pedido,
                produto=item.produto,
                quantidade=item.quantidade,
                preco_unitario=item.produto.preco
            )
        
        # Limpar o carrinho
        itens.delete()
        messages.success(request, "Pedido finalizado com sucesso!")
    else:
        messages.info(request, "Seu carrinho está vazio!")
    
    return redirect('nucleo:index')