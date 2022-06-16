from django.urls import path
from .views import (
    IndexView,
    ListarProdutosView,
    CriarProdutoView,
    AtualizarProdutoView,
    ExcluirProdutoView,
    CadastrarCategoriaView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('listar_produtos/', ListarProdutosView.as_view(), name='listarprod'),
    path('cadastro_produto/', CriarProdutoView.as_view(), name='addproduto'),
    path('atualizar_produto/<int:pk>', AtualizarProdutoView.as_view(),
         name='updateproduto'),
    path('excluir_produto/<int:pk>', ExcluirProdutoView.as_view(),
         name='delproduto'),
    path('cadastro_categoria/', CadastrarCategoriaView.as_view(), name='cadcateg'),
]
