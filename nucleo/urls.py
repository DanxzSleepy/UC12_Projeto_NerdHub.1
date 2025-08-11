from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/<int:id>/', views.detalhe_produto, name='detalhe_produto'),
    path('sobre/', views.sobre, name='sobre'),
    path('suporte/', views.suporte, name='suporte'),
    path('usuario/', include('usuarios.urls'), name='usuarios')

] 

