from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='marcas/', blank=True, null=True)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    imagem_principal = models.ImageField(upload_to='produtos/')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='produtos')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class ImagemProduto(models.Model):
    produto = models.ForeignKey(Produto, related_name='imagens_adicionais', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/adicionais/')

    def __str__(self):
        return f"Imagem extra de {self.produto.nome}"


# Loja e Users
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
class Review(models.Model):
    produto = models.ForeignKey(Produto, related_name='reviews', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()  # nome unificado
    nota = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])  # 1 a 5 estrelas
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.produto.nome} ({self.nota}⭐)"

class Estoque(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name='estoque')
    quantidade = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return f"Estoque de {self.produto.nome}: {self.quantidade}"

class Carrinho(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carrinho')

    def __str__(self):
        return f"Carrinho de {self.usuario.username}"

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    finalizado = models.BooleanField(default=False)

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    preco_unitario = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} no Pedido #{self.pedido.id}"