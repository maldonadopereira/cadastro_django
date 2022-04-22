from django.urls import path
from produtos import views

app_name = 'produtos'

urlpatterns = [
    path('list/', views.ProdutoList.as_view(), name='list'),
    path('create/', views.ProdutoCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ProdutoUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.ProdutoDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.ProdutoDelete.as_view(), name='delete'),

]