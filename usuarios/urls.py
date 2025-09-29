from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    
    path('conta/', views.conta, name='conta' ),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('sair/', views.user_logout, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('enderecos/', views.enderecos, name='enderecos'),
    path('enderecos/editar/<int:endereco_id>/', views.endereco_editar, name='endereco_editar'),
    path('enderecos/excluir/<int:endereco_id>/', views.endereco_excluir, name='endereco_excluir')
    
]