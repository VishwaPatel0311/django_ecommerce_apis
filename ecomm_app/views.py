from rest_framework import generics
from .models import Customer, Product
from .serializers import CustomerSerializer, ProductSerializer, Order, OrderSerializer


class CustomerListView(generics.ListCreateAPIView):
    try:
        queryset = Customer.objects.all()
        serializer_class = CustomerSerializer
    except Exception as e:
        print("Error in CustomerListView: {}".format(str(e)))


class CustomerDetailView(generics.RetrieveUpdateAPIView):
    try:
        queryset = Customer.objects.all()
        serializer_class = CustomerSerializer
    except Exception as e:
        print("Error in CustomerDetailView: {}".format(str(e)))


class ProductListView(generics.ListCreateAPIView):
    try:
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
    except Exception as e:
        print("Error in ProductListView: {}".format(str(e)))


class OrderListView(generics.ListCreateAPIView):
    try:
        queryset = Order.objects.all()
        serializer_class = OrderSerializer

        def get_queryset(self):
            queryset = super().get_queryset()
            products_param = self.request.query_params.get('products', None)
            customer_param = self.request.query_params.get('customer', None)

            if products_param:
                products = products_param.split(',')
                queryset = queryset.filter(order_item__product__name__in=products)

            if customer_param:
                queryset = queryset.filter(customer__name=customer_param)

            return queryset
    except Exception as e:
        print("Error in OrderListView: {}".format(str(e)))


class OrderDetailView(generics.RetrieveUpdateAPIView):
    try:
        queryset = Order.objects.all()
        serializer_class = OrderSerializer
    except Exception as e:
        print("Error in OrderDetailView: {}".format(str(e)))

