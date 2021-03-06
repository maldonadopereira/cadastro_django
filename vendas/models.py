from django.conf import settings
from django.db import models
from users.models import User
from produtos.models import Produto


class Venda(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    products = models.ManyToManyField(Produto, blank = True)
    total = models.DecimalField(default = 0.00, max_digits=100, decimal_places = 2)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.id)