from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def erro_404(request):
    return render(request, '404.html')


def erro_403(request):
    return None