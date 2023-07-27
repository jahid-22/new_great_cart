from django.shortcuts import render, redirect , get_object_or_404
from django.http import HttpResponse
from .models import Cart, Cart_Item
from store.models import Product
from django.db.models import Q

# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    if request.POST:
        for item in request.POST:
            key = item 
            value = request.POST[key] 
    
    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()

    try:
        cart_item = Cart_Item.objects.get(Q(product=product) & Q(cart=cart))
        cart_item.quantity += 1
        cart_item.save()
    except Cart_Item.DoesNotExist:
        cart_item = Cart_Item.objects.create(product=product, cart=cart, quantity=1)
        cart_item.save()

    return redirect('cart')

    # return HttpResponse(cart_item.quantity)
    # exit()   
    
def minus_card(request, product_id ):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        product = get_object_or_404(Product, id = product_id)

        cart_item = Cart_Item.objects.get(Q(product=product) & Q(cart=cart))
        cart_item.quantity -= 1
        cart_item.save()
    except Exception:
        pass
    return redirect('cart')  

set
def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    product = Product.objects.get(id = product_id)
    
    cart_item = Cart_Item.objects.get(Q(product=product) & Q(cart=cart))
    cart_item.delete()
    
    return redirect('cart')  


def cart(request):
    
    total = 0
    
    cart    = Cart.objects.get(cart_id = _cart_id(request))
    cart_items = Cart_Item.objects.filter(cart = cart, is_active = True)
    
   
    for cart_item in cart_items:
        total = (cart_item.product.price * cart_item.quantity)
        # quantity = cart_item.quantity
    
    tax = (2*total)/100
    grand_total = tax + total
    
    context = {
        'total':total,
        # 'quantity':quantity,
        'cart_item':cart_items,
        'tax':tax,
        'grand_total' :grand_total
    }    
    
    return render(request, 'cart/cart.html', context)

