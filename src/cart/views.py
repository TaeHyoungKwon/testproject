from django.shortcuts import render, redirect, get_object_or_404
from menus.models import Menu

from .models import Cart, CartItem
from .utils import _cart_id


def add_cart(request, menu_id):
    menu = Menu.objects.get(id=menu_id)
    cart, __ = Cart.objects.get_or_create(
        cart_id=_cart_id(request),
        user=request.user
    )
    cart_item, is_created = CartItem.objects.get_or_create(
        menu=menu,
        cart=cart,
        defaults={
            'quantity': '1',
        }
    )

    if not is_created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/cart/')


def cart_list(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)

        for cart_item in cart_items:
            total += (cart_item.menu.price * cart_item.quantity)
            counter += cart_item.quantity

    except:
        return render(request, 'cart/no_item.html', {})

    context = {
        'menu': cart_items, 'total': total, 'counter': counter
    }

    return render(request, 'cart/cart_list1.html', context)


def remove_cart_item(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(
        menu=menu,
        cart=cart
    )

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()

    else:
        cart_item.delete()

    return redirect('cart:cart_list')


def remove_all_cart_item(request, menu_id):
    menu = get_object_or_404(Menu, id=menu_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(
        menu=menu,
        cart=cart,
    )

    cart_item.delete()

    return redirect('cart:cart_list')


def remove_cart(request):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart.delete()

    return redirect('cart:cart_list')
