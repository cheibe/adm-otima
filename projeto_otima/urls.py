from django.contrib import admin
from django.urls import path
from app_otima import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    
    path('fornecedores/', views.fornecedores, name='fornecedores'),
    path('fornecedores/adicionar/', views.adicionar_fornecedor, name='adicionar_fornecedor'),
    path('fornecedores/editar/<fornecedor_id>/', views.editar_fornecedor, name='editar_fornecedor'),

    path('clientes/', views.clientes, name='clientes'),

    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuarios/adicionar/', views.adicionar_usuario, name='adicionar_user'),

    path('pagamentos/', views.pagamentos, name='pagamentos'),

    path('recebimentos/', views.recebimentos, name='recebimentos'),
]
