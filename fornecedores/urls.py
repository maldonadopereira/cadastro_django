from django.contrib.auth.decorators import login_required
from django.urls import path
from fornecedores import views

app_name = 'fornecedores'

urlpatterns = [
    path('list/', login_required(views.FornecedorList.as_view()), name='list'),
    path('create/', login_required(views.FornecedorCreate.as_view()), name='create'),
    path('update/<int:pk>/', login_required(views.FornecedorUpdate.as_view()), name='update'),
    path('detail/<int:pk>/', login_required(views.FornecedorDetail.as_view()), name='detail'),
    path('delete/<int:pk>/', login_required(views.FornecedorDelete.as_view()), name='delete'),
]