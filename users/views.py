from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView

from users.models import User




class UserDetail(DetailView):
    model = User
    queryset = User.objects.all()
    template_name = 'user_detail.html'



class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'telefone', 'cep', 'endereco', 'uf', 'cidade', 'foto_user']
    success_url = reverse_lazy('index')
    template_name = 'user_form.html'

