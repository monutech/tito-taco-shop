from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Product


def index(request):
    product_list = Product.objects.order_by('id')
    kennysmom = {
        'product_list': product_list,
    }
    return render(request, 'index.html', kennysmom)


# Create your views here.
def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context)
    return HttpResponse(f"You are looking at {product.name}. "
                        "Would you like to buy it? It's pretty awesome."
                        )


def get_image(request, product_id, filename):
    print(f"GETTING IMAGE: {filename}")
    product = Product.objects.get(id=product_id)
    image_data = product.image.open()
    return HttpResponse(image_data, content_type="image/gif")