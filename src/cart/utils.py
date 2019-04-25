def _cart_id(request):
    cart = request.session.session_key
    print(request.session.items())
    if not cart:
        cart = request.session.create()
    return cart
