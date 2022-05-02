from django.contrib.auth.decorators import login_required
from django.urls import path
from vendas import views

app_name = 'vendas'

urlpatterns = [
    path('venda', views.venda_home, name='venda'),

]