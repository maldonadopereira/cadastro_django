from produtos.models import Produto
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class ProdutoList(ListView):
    model = Produto
    queryset = Produto.objects.all()


class ProdutoCreate(CreateView):
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('produtos:list')

class ProdutoUpdate(UpdateView):
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('produtos:list')

class ProdutoDetail(DetailView):
    model = Produto
    queryset = Produto.objects.all()


class ProdutoDelete(DeleteView):
    model = Produto
    queryset = Produto.objects.all()
    success_url = reverse_lazy('produtos:list')
