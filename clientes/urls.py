from django.urls import path
from clientes import views

app_name = 'clientes'

urlpatterns = [
    path('list/', views.ClienteList.as_view(), name='list'),
    path('create/', views.ClienteCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.ClienteUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', views.ClienteDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', views.ClienteDelete.as_view(), name='delete'),

]