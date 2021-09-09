from rest_framework import serializers
from .models import Book, Cart, Customer
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password")

    def validate(self, args):
        email = args.get("email", None)
        username = args.get("username", None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": ("email already exists")})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": ("username already exists")})

        return super().validate(args)

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"
