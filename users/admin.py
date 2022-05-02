from django.contrib import admin

from users.models import User, Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'criacao')
    list_display_links = ('username',)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'conteudo', 'user')
    list_display_links = ('titulo',)
    exclude = ['user',]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super().save_model(request, obj, form, change)

'''    # Permite que apenas o autor veja a postagem
    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(user=request.user)
'''

