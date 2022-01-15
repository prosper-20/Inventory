from email import contentmanager
from django.shortcuts import render
from .models import Product, Order
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'dashboard/home.html')

@login_required(login_url='login')
def order(request):
    return render(request, 'dashboard/order.html')

def products(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'dashboard/products.html', context)

def staff(request):
    order = Order.objects.all()
    context = {
        "order": order
    }
    return render(request, 'dashboard/staff_index.html', context)
