from django.shortcuts import render
from rest_framework import permissions
from rest_framework import serializers
from rest_framework.serializers import Serializer
from DjangoApi.serializers import BookSerializer, CustomerSerializer, CartSerializer
from rest_framework import generics, viewsets
from .serializers import (
    RegistrationSerializer,
    BookSerializer,
    CartSerializer,
    CustomerSerializer,
    RegistrationSerializer,
)
from .models import Book, Customer, Cart
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
import uuid
from rest_framework import status


class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "RequestId": str(uuid.uuid4()),
                    "Message": "User created succesfully",
                    "User": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST
        )


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
