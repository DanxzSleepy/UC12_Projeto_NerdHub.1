import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nerdhub.settings')
django.setup()

from django.contrib.auth.models import User
from nucleo.models import Produto, Carrinho, ItemCarrinho

def test_cart_functionality():
    # Get the admin user
    user = User.objects.get(username='admin')
    print(f"Using user: {user.username}")
    
    # Get the first product
    produto = Produto.objects.first()
    print(f"Using product: {produto.nome}")
    
    # Create or get cart for user
    carrinho, created = Carrinho.objects.get_or_create(usuario=user)
    print(f"Cart created: {created}")
    
    # Add item to cart
    item, created = ItemCarrinho.objects.get_or_create(
        carrinho=carrinho,
        produto=produto,
        defaults={'quantidade': 1}
    )
    
    if not created:
        item.quantidade += 1
        item.save()
        print(f"Updated item quantity to: {item.quantidade}")
    else:
        print(f"Added new item with quantity: {item.quantidade}")
    
    # List items in cart
    itens = carrinho.itens.all()
    print(f"\nItems in cart:")
    total = 0
    for item in itens:
        item_total = item.produto.preco * item.quantidade
        total += item_total
        print(f"- {item.produto.nome}: {item.quantidade} x R${item.produto.preco} = R${item_total}")
    
    print(f"\nTotal cart value: R${total}")
    
    # Remove item from cart
    # item.delete()
    # print("Item removed from cart")

if __name__ == '__main__':
    test_cart_functionality()