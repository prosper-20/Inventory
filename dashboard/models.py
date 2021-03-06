from django.db import models

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Toiletries', 'Toiletries'),
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
    ('Household', 'Household')
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str__(self):
        return f'{self.name}'



class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f' {self.order_quantity} units of {self.product} ordered by {self.staff.username}'
