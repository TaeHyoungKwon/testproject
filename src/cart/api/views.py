from django.shortcuts import render
from django.http import JsonResponse
from ..models import Cart


def cart_menu_list_api(request):
    cart, new_or_not = Cart.objects.new_or_get(request)
    menus_in_cart = [
        {
            "id": menu.id,
            "title": menu.title,
            "price": menu.price
        }
        for menu in cart.menus.all()
    ]
    data = {
        "menu": menus_in_cart,
        "total": cart.get_total_price(),
    }
    return JsonResponse(data)
