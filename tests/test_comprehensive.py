import os
import django
import unittest
from unittest.mock import patch, MagicMock
import sys

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nerdhub.settings')
django.setup()

from django.contrib.auth.models import User
from django.test import TestCase, Client
from nucleo.models import Produto, Marca, Categoria, Carrinho, ItemCarrinho, Review, Estoque
from usuarios.models import Perfil

class NerdHubTestCase(TestCase):
    def setUp(self):
        """Set up test dependencies"""
        # Clean up any existing test data first
        User.objects.filter(username='testuser').delete()
        User.objects.filter(username='newuser').delete()
        Marca.objects.filter(nome='Marvel').delete()
        Categoria.objects.filter(nome='Action Figures').delete()
        
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword123'
        )
        
        # Create test profile
        self.perfil, created = Perfil.objects.get_or_create(user=self.user)
        
        # Create test brand and category
        self.marca, created = Marca.objects.get_or_create(nome='Marvel')
        self.categoria, created = Categoria.objects.get_or_create(nome='Action Figures')
        
        # Create test product
        self.produto, created = Produto.objects.get_or_create(
            nome='Spider-Man Action Figure',
            defaults={
                'descricao': 'High-quality Spider-Man action figure',
                'preco': 199.90,
                'marca': self.marca,
                'categoria': self.categoria
            }
        )
        
        # Create stock for the product
        self.estoque, created = Estoque.objects.get_or_create(
            produto=self.produto,
            defaults={'quantidade': 10}
        )
        
        # Create test client
        self.client = Client()
        
    def tearDown(self):
        """Clean up after tests"""
        # Clean up in reverse order of creation to avoid foreign key issues
        ItemCarrinho.objects.filter(carrinho__usuario=self.user).delete()
        Carrinho.objects.filter(usuario=self.user).delete()
        Review.objects.filter(usuario=self.user).delete()
        Estoque.objects.filter(produto=self.produto).delete()
        Produto.objects.filter(id=self.produto.id).delete()
        Perfil.objects.filter(user=self.user).delete()
        User.objects.filter(id=self.user.id).delete()
        Marca.objects.filter(id=self.marca.id).delete()
        Categoria.objects.filter(id=self.categoria.id).delete()

    def test_user_registration(self):
        """Test user registration functionality"""
        # Ensure test user doesn't exist
        User.objects.filter(username='newuser').delete()
        
        response = self.client.post('/usuario/cadastro/', {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'senha': 'newpassword123'
        })
        
        # Check if user was created
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='newuser').exists())
        
    def test_user_login(self):
        """Test user login functionality"""
        response = self.client.post('/usuario/conta/', {
            'username': 'testuser',
            'senha': 'testpassword123'
        })
        
        # Check if login was successful
        self.assertEqual(response.status_code, 302)  # Redirect after successful login
        
    def test_product_detail_view(self):
        """Test product detail page"""
        response = self.client.get(f'/produto/{self.produto.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.produto.nome)
        
    def test_add_to_cart(self):
        """Test adding product to cart"""
        # Login first
        self.client.login(username='testuser', password='testpassword123')
        
        # Add product to cart
        response = self.client.post(f'/adicionar-ao-carrinho/{self.produto.id}/')
        
        # Check if product was added to cart
        self.assertEqual(response.status_code, 302)  # Redirect after adding to cart
        carrinho = Carrinho.objects.get(usuario=self.user)
        self.assertTrue(ItemCarrinho.objects.filter(carrinho=carrinho, produto=self.produto).exists())
        
    def test_remove_from_cart(self):
        """Test removing product from cart"""
        # Login first
        self.client.login(username='testuser', password='testpassword123')
        
        # Add product to cart first
        carrinho, created = Carrinho.objects.get_or_create(usuario=self.user)
        item = ItemCarrinho.objects.create(carrinho=carrinho, produto=self.produto, quantidade=1)
        
        # Remove item from cart
        response = self.client.post(f'/remover-item-carrinho/{item.id}/')
        
        # Check if item was removed
        self.assertEqual(response.status_code, 302)  # Redirect after removal
        self.assertFalse(ItemCarrinho.objects.filter(id=item.id).exists())
        
    def test_checkout_process(self):
        """Test checkout process"""
        # Login first
        self.client.login(username='testuser', password='testpassword123')
        
        # Add product to cart
        carrinho, created = Carrinho.objects.get_or_create(usuario=self.user)
        ItemCarrinho.objects.create(carrinho=carrinho, produto=self.produto, quantidade=1)
        
        # Proceed to checkout
        response = self.client.post('/finalizar-pedido/')
        
        # Check if checkout was successful
        self.assertEqual(response.status_code, 302)  # Redirect after checkout
        # Cart should be empty after checkout
        self.assertEqual(carrinho.itens.count(), 0)
        
    def test_add_review(self):
        """Test adding a product review"""
        # Login first
        self.client.login(username='testuser', password='testpassword123')
        
        # Add review
        response = self.client.post(f'/adicionar-review/{self.produto.id}/', {
            'texto': 'Great product!',
            'nota': 5
        })
        
        # Check if review was added
        self.assertEqual(response.status_code, 302)  # Redirect after adding review
        self.assertTrue(Review.objects.filter(usuario=self.user, produto=self.produto).exists())

if __name__ == '__main__':
    unittest.main()