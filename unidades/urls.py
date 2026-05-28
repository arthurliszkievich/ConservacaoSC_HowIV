from django.urls import path
from . import views

urlpatterns = [
    # ---- PÁGINAS PÚBLICAS ----
    path('', views.index, name='index'),
    path('detalhes/<int:unidade_id>/', views.detalhes, name='detalhes'),
    path('comunicacao/<int:unidade_id>/', views.comunicacao, name='comunicacao'),

    # ---- AUTENTICAÇÃO ----
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # ---- PAINEL DO USUÁRIO ----
    path('painel/', views.painel_view, name='painel'),
    path('painel/nova/', views.nova_unidade_view, name='nova_unidade'),
    path('painel/editar/<int:unidade_id>/', views.editar_unidade_view, name='editar_unidade'),
    path('painel/apagar/<int:unidade_id>/', views.apagar_unidade_view, name='apagar_unidade'),
    path('painel/nova-instituicao/', views.nova_instituicao_view, name='nova_instituicao'),
    path('painel/novo-municipio/', views.novo_municipio_view, name='novo_municipio'),

]
