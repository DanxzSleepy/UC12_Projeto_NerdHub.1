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

    def __str__(self):
        return self.nome

class ImagemProduto(models.Model):
    produto = models.ForeignKey(Produto, related_name='imagens_adicionais', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='produtos/adicionais/')

    def __str__(self):
        return f"Imagem extra de {self.produto.nome}"
