from django.contrib.auth.decorators import login_required
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    #path('accounts/profile/<int:user_id>', views.profile, name='profile'),
   # path('atualiza_cadastro/<int:user_id>', views.atualiza_cadastro, name='atualiza_cadastro'),
    path('update/<int:pk>/', login_required(views.UserUpdate.as_view()), name='update'),
    path('detail/<int:pk>/', login_required(views.UserDetail.as_view()), name='detail'),

]