from rest_framework import permissions
from DjangoApi.serializers import BookSerializer, CustomerSerializer, CartSerializer
from rest_framework import generics, viewsets
from .serializers import BookSerializer, CartSerializer, CustomerSerializer
from .models import Book, Customer, Cart
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class CartView(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
