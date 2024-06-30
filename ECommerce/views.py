from django.shortcuts import render
from products.models import Product

def index(request):
    all_products = Product.objects.all()
    return render(request, "base.html", {'products': all_products})
