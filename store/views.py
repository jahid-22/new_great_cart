from django.shortcuts import render, get_object_or_404
from . models import Product, Catagory , Product_variation
from django.core.paginator import Paginator
from cart.models import Cart, Cart_Item
from django.http import HttpResponse
from cart.views import _cart_id

# Create your views here.

def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products' : products,
    }
    return render(request, 'home.html', context)


def product_detail (request, category_slug, product_slug):
    
    single_product = Product.objects.get(catagory__slug=category_slug, slug=product_slug)
    already_in_cart = Cart_Item.objects.filter(cart__cart_id = _cart_id(request), product=single_product).exists()
    
    product_variation_color  = Product_variation.objects.filter(category = 'color')
    product_variation_size  = Product_variation.objects.filter(category = 'size')
    
    
    context =  {
        'single_product' : single_product,
        'already_in_cart' : already_in_cart,
        'product_variation_color' : product_variation_color,
        'product_variation_size' : product_variation_size
    }
    return render(request, 'prod_details.html', context)


def store(request, category_slug=None):
    if category_slug is None:
        get_all_product = Product.objects.all().order_by('-id')
        pagination = Paginator(get_all_product, 5)
        page_number = request.GET.get('page')
        page_obj = pagination.get_page(page_number)
    else:
        get_all_product = Product.objects.filter(catagory__slug=category_slug)

        paginator = Paginator(get_all_product, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    
    context = {
        # 'get_all_product' : page_obj,
        'page_obj' : page_obj,
    }
    return render(request, 'store.html', context)


def add_cart(request, id):
    
    get_produts = Products.objects.get(id=id)
    context = {
        'get_produts' : get_produts
    }
    return render (request, 'cart.html', context)

