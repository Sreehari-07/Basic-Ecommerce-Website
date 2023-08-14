from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:product_id>/', views.remove_cart, name='remove_cart'),  # Add this line
    path('', views.cart_detail, name='cart_detail'),
    path('remove_single_item/<int:product_id>/', views.remove_single_item, name='remove_single_item'),

]
