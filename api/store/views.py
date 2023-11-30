from django.shortcuts import render

from .models import Product


# Create your views here.
def index(request):
    context = {
        'living_room': Product.objects.filter(category__name="Living Room"),
        'home_office': Product.objects.filter(category__name="Home Office")
    }
    return render(request, 'index.html', context=context)