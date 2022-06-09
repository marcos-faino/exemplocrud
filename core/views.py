from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from core.models import Produto


class IndexView(TemplateView):
    template_name = 'index.html'


class ListarProdutosView(ListView):
    model = Produto
    template_name = 'listarprodutos.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'