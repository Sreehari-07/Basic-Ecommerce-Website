from django.shortcuts import render, redirect
from shop.models import Product
from .models import Cart, Cart_Item
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

def _cart_id(request):
     cart = request.session.session_key
     if not cart:
          cart = request.session.create()
     return cart

def add_cart(request, product_id):
     product = Product.objects.get(id=product_id)
     try:
          cart = Cart.objects.get(cart_id=_cart_id(request))
     except Cart.DoesNotExist:
          cart = Cart.objects.create(
               cart_id = _cart_id(request)
          )
          cart.save()
     try:
          cart_item = Cart_Item.objects.get(product=product, cart=cart)
          cart_item.quantity += 1
          cart_item.save()
     except Cart_Item.DoesNotExist:
          cart_item = Cart_Item.objects.create(
               product = product,
               quantity = 1,
               cart = cart
          )
          cart_item.save()
     return redirect('cart:cart_detail')

def cart_detail(request, total=0, counter=0, cart_items=None):
     try:
          cart = Cart.objects.get(cart_id=_cart_id(request))
          cart_items = Cart_Item.objects.filter(cart=cart, active=True)
          for cart_item in cart_items:
               total += (cart_item.product.price * cart_item.quantity)
               counter += cart_item.quantity

     except ObjectDoesNotExist:
          pass
     return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))


def remove_cart(request, product_id):
     cart = Cart.objects.get(cart_id=_cart_id(request))
     product = Product.objects.get(id=product_id)

     try:
          cart_item = Cart_Item.objects.get(product=product, cart=cart)
          cart_item.delete()
     except Cart_Item.DoesNotExist:
          pass

     return redirect('cart:cart_detail')


def remove_single_item(request, product_id):
     cart = Cart.objects.get(cart_id=_cart_id(request))
     product = get_object_or_404(Product, id=product_id)

     try:
          cart_item = Cart_Item.objects.get(product=product, cart=cart)
          if cart_item.quantity > 1:
               cart_item.quantity -= 1
               cart_item.save()
     except Cart_Item.DoesNotExist:
          pass

     return redirect('cart:cart_detail')
