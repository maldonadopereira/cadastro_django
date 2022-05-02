from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('erro_404', views.erro_404, name='404'),
    path('erro_403', views.erro_403, name='403'),
]