from multiprocessing import context
from django.shortcuts import render
from django.views.generic import TemplateView
from products.models import Kitobjanri, Product
from django.shortcuts import get_list_or_404


# class MainView(TemplateView):
#     template_name = 'index.html'

def main_view(request):
    janrlar = Kitobjanri.objects.all()
    products = get_list_or_404(Product, status = True)[:3]

    context = {
        "janrlar":janrlar,
        "products": products
    }

    return render(request=request, template_name='index.html', context=context)

def contact(request):
    return render(request=request, template_name='contact.html')

def about_us(request):
    return render(request=request, template_name='about_us.html')

def grid_view(request):

    janrlar = Kitobjanri.objects.all()
    products = get_list_or_404(Product, status = True)[:18]

    context = {
        "janrlar":janrlar,
        "products": products
    }
    return render(request=request, template_name='grid-view.html', context=context)

def three_col(request):
    janrlar = Kitobjanri.objects.all()
    products = get_list_or_404(Product, status = True)[:18]

    context = {
        "janrlar":janrlar,
        "products": products
    }
    return render(request=request, template_name='three-col.html', context=context)

def four_col(request):
    janrlar = Kitobjanri.objects.all()
    products = get_list_or_404(Product, status = True)[:16]

    context = {
        "janrlar":janrlar,
        "products": products
    }
    return render(request=request, template_name='four-col.html', context=context)

def list_view(request):
    janrlar = Kitobjanri.objects.all()
    products = get_list_or_404(Product, status = True)[:10]

    context = {
        "janrlar":janrlar,
        "products": products
    }
    return render(request=request, template_name='list-view.html', context=context)
