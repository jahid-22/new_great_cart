from django.shortcuts import render, get_object_or_404
from . models import Product, Catagory
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('-id')
    context = {
        'products' : products
    }
    return render(request, 'home.html', context)


def product_detail (request, category_slug, product_slug):
    
    single_product = Product.objects.get(catagory__slug=category_slug, slug=product_slug)
    context =  {
        'single_product' : single_product
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
        'get_all_product' : page_obj,
        # 'page_obj' : page_obj,
    }
    return render(request, 'store.html', context)


# def store(request, category_slug=None):
#     if category_slug is None:
#         get_all_product = Product.objects.all().order_by('-id')
#         selected_category = "All"  # Set a flag to indicate that all products are selected
#     else:
#         category = get_object_or_404(Category, slug=category_slug)
#         get_all_product = Product.objects.filter(category=category).order_by('-id')
#         selected_category = category.name  # Store the name of the selected category

#     pagination = Paginator(get_all_product, 2)  # Show 2 products per page
#     page_number = request.GET.get('page')
#     page_obj = pagination.get_page(page_number)

#     categories = Catagory.objects.all()  # Fetch all categories to display in the sidebar

#     context = {
#         'page_obj': page_obj,
#         'categories': categories,
#         'selected_category': selected_category,
#     }
#     return render(request, 'store.html', context)


def add_cart(request, id):
    get_produts = Products.objects.get(id=id)
    context = {
        'get_produts' : get_produts
    }
    return render (request, 'cart.html', context)
