from django.contrib import admin
from . models import Cart, Cart_Item
# Register your models here.

admin.site.register(Cart)

@admin.register(Cart_Item)
class AdminCart_item(admin.ModelAdmin):
    list_display = ['id','product','quantity']


