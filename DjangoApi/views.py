from rest_framework import permissions
from DjangoApi.serializers import BookSerializer, CustomerSerializer
from rest_framework import generics, viewsets
from .serializers import BookSerializer, CustomerSerializer
from .models import Book, Customer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class CustomerView(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
