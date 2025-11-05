from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    
    path('conta/', views.conta, name='conta' ),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('sair/', views.user_logout, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/seguranca/', views.perfil_seguranca, name='perfil_seguranca'),
    path('perfil/endereco/', views.perfil_endereco, name='perfil_endereco'),
    path('perfil/preferencias/', views.perfil_preferencias, name='perfil_preferencias'),
    path('perfil/privacidade/', views.perfil_privacidade, name='perfil_privacidade'),
    path('perfil/conta/', views.perfil_conta, name='perfil_conta'),
    path('enderecos/', views.enderecos, name='enderecos'),
    path('enderecos/editar/<int:endereco_id>/', views.endereco_editar, name='endereco_editar'),
    path('enderecos/excluir/<int:endereco_id>/', views.endereco_excluir, name='endereco_excluir')
    
]