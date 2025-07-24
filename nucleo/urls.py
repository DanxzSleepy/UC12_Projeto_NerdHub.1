from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/<int:id>/', views.detalhe_produto, name='detalhe_produto'),
]