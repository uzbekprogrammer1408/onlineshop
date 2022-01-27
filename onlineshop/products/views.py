from django.shortcuts import render, redirect
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

def products(request):
    janrlar = Kitobjanri.objects.all()
    products = get_list_or_404(Product, status = True)[:18]

    context = {
        "janrlar":janrlar,
        "products": products
    }
    return render(request, 'products.html', context=context)