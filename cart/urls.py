from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name="cart"),
    path('add-cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('minus_card/<int:product_id>/', views.minus_card, name='minus_card'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_card'),
]
