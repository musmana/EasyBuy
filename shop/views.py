from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    newest = Product.objects.all()[:6]
    return render(request, "home.html", {"newest": newest})

def product_list(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "product_detail.html", {"product": product})
