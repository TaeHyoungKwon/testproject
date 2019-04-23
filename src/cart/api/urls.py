from django.urls import path

from . import views

urlpatterns = [
    path(
        '',
        views.cart_menu_list_api,
        name='cart_list_api'
    )
]
