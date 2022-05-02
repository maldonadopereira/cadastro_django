from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DetailView, CreateView, ListView

from users.models import User, Post




class UserDetail(LoginRequiredMixin, DetailView):
    model = User
    queryset = User.objects.all()
    template_name = 'user_detail.html'



class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'telefone', 'cep', 'endereco', 'uf', 'cidade', 'foto_user']
    success_url = reverse_lazy('index')
    template_name = 'user_form.html'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    #fields = '__all__'
    fields = ['titulo', 'conteudo', 'ativo']
    success_url = reverse_lazy('users:post_list')
    template_name = 'post_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('users:post_detail')
    template_name = 'post_form.html'

class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'post_detail.html'

class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'post_list.html'

    def get_queryset(self):
        self.object_list = Post.objects.filter(user=self.request.user)
        return self.object_list
