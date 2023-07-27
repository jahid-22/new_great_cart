from django.db import models
from account.models import Person
from store.models import Product
# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=300, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
class Cart_Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart    = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity= models.PositiveIntegerField(default=1)
    is_active= models.BooleanField(default=True)
    
    def sub_total(self):
        return self.quantity * self.product.price
    
    
    def __str__(self):
        return str(self.product.product_name)
     

