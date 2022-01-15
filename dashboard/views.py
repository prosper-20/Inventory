from email import contentmanager
from django.shortcuts import render
from .models import Product

# Create your views here.


def home(request):
    return render(request, 'dashboard/home.html')

def order(request):
    return render(request, 'dashboard/order.html')

def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'dashboard/products.html', context)
