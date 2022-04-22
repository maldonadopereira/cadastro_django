from django.urls import path
from fornecedores import views

app_name = 'fornecedores'

urlpatterns = [
    path('list/', views.FornecedorList.as_view(), name='list'),
    path('create/', views.FornecedorCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.FornecedorUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.FornecedorDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.FornecedorDelete.as_view(), name='delete'),
]