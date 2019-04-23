from django.shortcuts import render


def cart_list(request):
    context = {
        "count": 1,
        "name": "kwon"
    }
    return render(request, 'cart/cart_list.html', context)
