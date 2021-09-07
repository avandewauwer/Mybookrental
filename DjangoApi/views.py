from DjangoApi.serializers import BookSerializer
from rest_framework import generics, viewsets
from .serializers import BookSerializer
from .models import Book


class BookView(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
