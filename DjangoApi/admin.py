from django.contrib import admin
from .models import Book, Customer, Cart

# Register your models here.
admin.site.register(Book)
admin.site.register(Customer)
admin.site.register(Cart)
