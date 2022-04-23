from django.contrib.auth.decorators import login_required
from django.urls import path
from produtos import views

app_name = 'produtos'

urlpatterns = [
    path('list/', login_required(views.ProdutoList.as_view()), name='list'),
    path('create/', login_required(views.ProdutoCreate.as_view()), name='create'),
    path('update/<int:pk>/', login_required(views.ProdutoUpdate.as_view()), name='update'),
    path('detail/<int:pk>/', login_required(views.ProdutoDetail.as_view()), name='detail'),
    path('delete/<int:pk>/', login_required(views.ProdutoDelete.as_view()), name='delete'),

]