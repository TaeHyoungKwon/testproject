from django.shortcuts import render
from django.http import JsonResponse
from ..models import Cart


def cart_menu_list_api(request):
    cart, new_or_not = Cart.objects.new_or_get(request)
    print(cart, new_or_not)
    menus_in_cart = [
        {
            "id": menu.id,
            "name": menu.name,
            "price": menu.price
        }
        for menu in cart.menus.all()
    ]
    data = {
        "menu": menus_in_cart,
        "total": cart.total,
    }
    return JsonResponse(data)
