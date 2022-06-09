from django.urls import path
from .views import IndexView, ListarProdutosView




urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('listar_produtos/', ListarProdutosView.as_view(), name='listarprod'),
]
