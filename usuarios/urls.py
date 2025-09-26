from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    
    path('conta/', views.conta, name='conta' ),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('sair/', views.user_logout, name='logout')
    
]