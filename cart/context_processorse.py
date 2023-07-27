from . views import _cart_id
from .models import Cart , Cart_Item

def counter(request):
    count_item = 0
    if 'admin' in request.path:
        return {}
    else:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = Cart_Item.objects.filter(cart = cart)
        
        for cart_item in cart_items:
            count_item += cart_item.quantity
        
    return dict(count_item = count_item)