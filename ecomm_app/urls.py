# ecommerce_app/urls.py
from django.urls import path
from .views import (CustomerListView, CustomerDetailView, ProductListView, OrderListView,
                    OrderDetailView)

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),

]
