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