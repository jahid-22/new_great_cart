from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('product_detail/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name="product_detail"),
    path('add_cart/<int:id>/', views.add_cart, name='add_cart'),
    path('store/', views.store, name="store"),
    path('store/<slug:category_slug>/', views.store, name="products_by_cata"),
]
