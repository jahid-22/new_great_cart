from django.db import models
from django.urls import reverse

# Create your models here.

class Catagory(models.Model):
    catagory_name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Catagory'
        verbose_name_plural = 'Catagories'
    
    def __str__(self):
        return self.slug
    
    def get_absolute_url(self):
        return reverse("products_by_cata", args=[self.slug])
    

class Product(models.Model):
    product_name    = models.CharField(max_length=200)
    slug            = models.SlugField(max_length=200)
    description     = models.TextField(blank=True)
    price           = models.IntegerField()
    img_url         = models.CharField(max_length=400, default='image url')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    catagory        = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detail', args=[self.catagory.slug, self.slug])
    
    @property
    def get_id (self):
        return self.id
    
    def __str__(self):
        return self.product_name

