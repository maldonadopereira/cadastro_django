from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from fornecedores.models import Fornecedor


class FornecedorList(ListView):
    model = Fornecedor
    queryset = Fornecedor.objects.all()
    template_name = 'fornecedor_list.html'


class FornecedorCreate(CreateView):
    model = Fornecedor
    fields = '__all__'
    success_url = reverse_lazy('fornecedores:list')
    template_name = 'fornecedor_form.html'

class FornecedorUpdate(UpdateView):
    model = Fornecedor
    fields = '__all__'
    success_url = reverse_lazy('fornecedores:list')
    template_name = 'fornecedor_form.html'


class FornecedorDetail(DetailView):
    model = Fornecedor
    queryset = Fornecedor.objects.all()
    template_name = 'fornecedor_detail.html'



class FornecedorDelete(DeleteView):
    model = Fornecedor
    queryset = Fornecedor.objects.all()
    success_url = reverse_lazy('fornecedores:list')
