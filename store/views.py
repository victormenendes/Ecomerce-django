from django.shortcuts import render

from .models import Produto

def all_products(request):
    produtos = Produto.objects.all()
    return render(request, 'store/base.html', {'produtos': produtos})

def produto1(request):
    return render(request, 'store/produto1.html')

def produto2(request):
    return render(request, 'store/produto2.html')

def produto3(request):
    return render(request, 'store/produto3.html')

def produto4(request):
    return render(request, 'store/produto4.html')

def produto5(request):
    return render(request, 'store/produto5.html')

def produto6(request):
    return render(request, 'store/produto6.html')

def produto7(request):
    return render(request, 'store/produto7.html')

def produto8(request):
    return render(request, 'store/produto8.html')

