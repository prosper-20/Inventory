from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity')

admin.site.site_header = "Prosper's Inventory"

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)


