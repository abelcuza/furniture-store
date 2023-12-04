from django.shortcuts import render, get_object_or_404

from .models import Product, Category, Deals


# Create your views here.
def index(request):
    context = {

        'living_room': Product.objects.filter(category__name="Living Room"),
        'home_office': Product.objects.filter(category__name="Home Office")
    }
    return render(request, 'index.html', context=context)


def products(request):
    context = {
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
        'deals': Deals.objects.all(),
        'most_rated': Product.objects.order_by("-rate")
    }
    return render(request, 'products.html', context=context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, 'product-detail.html', context=context)
