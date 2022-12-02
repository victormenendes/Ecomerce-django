from django.shortcuts import render

from .models import Produto

def all_products(request):
    produtos = Produto.objects.all()
    return render(request, 'store/index.html', {'produtos': produtos})

