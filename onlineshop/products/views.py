from unicodedata import category
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from .models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from products.models import Kitobjanri, Product
from django.shortcuts import get_list_or_404

@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_detail(request):
    return render(request, 'cart.html')

def products(request, janr_slug=None):
    janr = None
    janrlar = Kitobjanri.objects.all()
    products = Product.objects.filter(status = True)[:18]

    if janr_slug:
        janr = get_object_or_404(Kitobjanri, slug=janr_slug)
        products = get_list_or_404(Product, janr=janr)

    context = {
        "janr":janr,
        "janrlar":janrlar,
        "products": products
    }
    return render(request, 'products.html', context=context)

def product_details(request, id):
    product = Product.objects.get(id=id)
    janrlar = Kitobjanri.objects.all()
    products = Product.objects.all()

    context = {
        "product": product,
        "janrlar": janrlar,
        "products": products
    }
    return render(request, 'product_details.html', context=context)

