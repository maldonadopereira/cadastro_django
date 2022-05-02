from produtos.models import Produto
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView


class ProdutoList(ListView):
    model = Produto
    queryset = Produto.objects.all()
    template_name = 'produto_list.html'


class ProdutoCreate(CreateView):
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('produtos:list')
    template_name = 'produto_form.html'

class ProdutoUpdate(UpdateView):
    model = Produto
    fields = '__all__'
    success_url = reverse_lazy('produtos:list')
    template_name = 'produto_form.html'

class ProdutoDetail(DetailView):
    model = Produto
    queryset = Produto.objects.all()
    template_name = 'produto_detail.html'


class ProdutoDelete(DeleteView):
    model = Produto
    queryset = Produto.objects.all()
    success_url = reverse_lazy('produtos:list')
    template_name = 'produto_confirm_delete.html'
