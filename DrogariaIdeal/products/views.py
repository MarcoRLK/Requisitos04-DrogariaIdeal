from django.shortcuts import render

from .forms import Create_Product_Form
from .models import Product
# Create your views here.


def create_product(request):
    if request.method == "POST":
        form = Create_Product_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request, 'create_product.html', {'form': form})

    else:
        form = Create_Product_Form()
        return render(request, 'create_product.html', {'form': form})


def list_products(request):
    context = {
        'all_products': Product.objects.all(),
    }
    return render(request, 'list_products.html', context)
