from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("order/", views.order, name="order"),
    path('products/', views.products, name="products"),
#     path('products/delete/<int:pk>/', views.product_delete,
#          name='dashboard-products-delete'),
#     path('products/detail/<int:pk>/', views.product_detail,
#          name='dashboard-products-detail'),
#     path('products/edit/<int:pk>/', views.product_edit,
#          name='dashboard-products-edit'),
#     path('customers/', views.customers, name='dashboard-customers'),
#     path('customers/detial/<int:pk>/', views.customer_detail,
#          name='dashboard-customer-detail'),
    path('order/', views.order, name='dashboard-order'),

]