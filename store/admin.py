from django.contrib import admin
from .models import Product , Catagory
# Register your models here.

@admin.register(Catagory)
class Admin_category (admin.ModelAdmin):
    list_display = ['catagory_name']
    prepopulated_fields = {'slug':['catagory_name']}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name','stock','catagory','is_available']
    prepopulated_fields = {'slug':('product_name',)}# automatically fill slug field
    search_fields = ['catagory']
