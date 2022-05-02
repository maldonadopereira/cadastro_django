from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from clientes.models import Cliente


class ClienteList(ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    template_name = 'cliente_list.html'


class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('clientes:list')
    template_name = 'cliente_form.html'


class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('clientes:list')
    template_name = 'cliente_form.html'


class ClienteDetail(DetailView):
    model = Cliente
    queryset = Cliente.objects.all()
    template_name = 'cliente_detail.html'



class ClienteDelete(DeleteView):
    model = Cliente
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('clientes:list')
    template_name = 'cliente_confirm_delete.html'
