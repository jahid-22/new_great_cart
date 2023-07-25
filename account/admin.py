from django.contrib import admin
from . models import Country , Person
# Register your models here.

@admin.register(Country)
class AdminCountry (admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    

@admin.register(Person)
class AdminPerson(admin.ModelAdmin):
    list_display = ['first_name', 'country']
    search_fields = ['country']
    
