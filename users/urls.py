from django.contrib.auth.decorators import login_required
from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [

    path('update/<int:pk>/', login_required(views.UserUpdate.as_view()), name='update'),
    path('detail/<int:pk>/', login_required(views.UserDetail.as_view()), name='detail'),
    path('post/create/', login_required(views.PostCreate.as_view()), name='post_create'),
    path('post/update/<int:pk>/', login_required(views.PostUpdate.as_view()), name='post_update'),
    path('post/detail/<int:pk>/', login_required(views.PostDetail.as_view()), name='post_detail'),
    path('post/list/', login_required(views.PostList.as_view()), name='post_list'),

]