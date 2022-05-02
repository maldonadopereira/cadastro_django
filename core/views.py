from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


def erro_404(request):
    return render(request, '404.html')


def erro_403(request):
    return None