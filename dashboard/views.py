from email import contentmanager
from django.shortcuts import render, redirect
from .models import Product, Order
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'dashboard/home.html')

@login_required(login_url='login')
def order(request):
    order = Order.objects.all()
    context = {
        "order": order,
    }
    return render(request, 'dashboard/order.html', context)

# def products(request):
#     products = Product.objects.all()
#     context = {
#         'products': products,
#     }
#     return render(request, 'dashboard/products.html', context)


def products(request):
    product = Product.objects.all()
    product_count = product.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    order = Order.objects.all()
    order_count = order.count()
    product_quantity = Product.objects.filter(name='')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('home')
    else:
        form = ProductForm()
    context = {
        'product': product,
        'form': form,
        'customer_count': customer_count,
        'product_count': product_count,
        'order_count': order_count,
    }
    return render(request, 'dashboard/products.html', context)

def staff(request):
    order = Order.objects.all()
    context = {
        "order": order
    }
    return render(request, 'dashboard/staff_index.html', context)
