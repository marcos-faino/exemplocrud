from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.models import Produto, Categoria


class IndexView(TemplateView):
    template_name = 'index.html'


class ListarProdutosView(ListView):
    model = Produto
    template_name = 'listarprodutos.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'


class CriarProdutoView(CreateView):
    model = Produto
    template_name = 'formproduto.html'
    fields = ['descricao', 'preco', 'quantidade', 'categoria']
    success_url = reverse_lazy('listarprod')


class AtualizarProdutoView(UpdateView):
    model = Produto
    template_name = 'formproduto.html'
    fields = ['descricao', 'preco', 'quantidade','categoria']
    success_url = reverse_lazy('listarprod')


class ExcluirProdutoView(DeleteView):
    model = Produto
    template_name = 'excluirproduto.html'
    success_url = reverse_lazy('listarprod')


class CadastrarCategoriaView(CreateView):
    model = Categoria
    template_name = 'cadastrarcateg.html'
    fields = ['descricao']
    success_url = reverse_lazy('cadcateg')
