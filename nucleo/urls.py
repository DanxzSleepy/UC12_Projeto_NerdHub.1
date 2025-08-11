from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/<int:id>/', views.detalhe_produto, name='detalhe_produto'),
    path('sobre/', views.sobre, name='sobre'),
    path('suporte/', views.suporte, name='suporte'),
    path('usuario/', include('usuarios.urls'), name='usuarios'),
    path('marca/<str:marca_nome>/', views.produtos_por_marca, name='produtos_por_marca'),
]