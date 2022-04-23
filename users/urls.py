from django.contrib.auth.decorators import login_required
from django.urls import path
from users import views



urlpatterns = [
    path('accounts/profile/<int:user_id>', views.profile, name='profile'),
    path('cadastro/<int:user_id>', views.completa_cadastro, name='completa_cadastro'),
    path('atualiza_cadastro/<int:user_id>', views.atualiza_cadastro, name='atualiza_cadastro'),

]