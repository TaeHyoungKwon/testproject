from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path(
        '<int:menu_id>/',
        views.add_cart,
        name='add_cart'
    ),
    path(
        '',
        views.cart_list,
        name='cart_list'
    ),
    path(
        '<int:menu_id>/remove/',
        views.remove_cart_item,
        name='remove_cart_item'
    ),
    path(
        '<int:menu_id>/remove_all/',
        views.remove_all_cart_item,
        name='remove_all_cart_item'
    ),
    path(
        'remove_cart/',
        views.remove_cart,
        name='remove_cart'
    ),
]
