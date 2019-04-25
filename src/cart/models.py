from decimal import Decimal
from django.conf import settings
from django.db import models

from config.common_datetime_model import CommonDateTime
from menus.models import Menu
from .utils import _cart_id

User = settings.AUTH_USER_MODEL

# class CartManager(models.Manager):
#     def new_or_get(self, request):
#         cart_id = request.session.get("cart_id", None)
#         qs = self.get_queryset().filter(id=cart_id)
#         if qs.count() == 1:
#             new_obj = False
#             cart_obj = qs.first()
#             if request.user.is_authenticated and cart_obj.user is None:
#                 cart_obj.user = request.user
#                 cart_obj.save()
#         else:
#             new_obj = True
#             cart_obj = Cart.objects.new(user=request.user)
#             request.session['cart_id'] = cart_obj.id
#         return cart_obj, new_obj

#     def new(self, user=None):
#         user_obj = None
#         if user is not None:
#             if user.is_authenticated:
#                 user_obj = user
#         return self.model.objects.create(user=user_obj)


class Cart(CommonDateTime):
    user = models.ForeignKey(
        User,
        verbose_name="유저",
        on_delete=models.CASCADE
    )
    cart_id = models.CharField("카트 아이디", max_length=100)

    class Meta:
        ordering = ['createa_at']

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.menu.title + " - " + str(self.quantity)

    def calc_sub_total_price(self):
        print("kwon")
        return self.menu.price * self.quantity

    def calc_total_price(self, total=0):
        print("tae")
        cart = Cart.objects.get(cart_id=self.cart.cart_id)
        cart_items = CartItem.objects.filter(cart=cart)

        for cart_item in cart_items:
            total += (cart_item.menu.price * cart_item.quantity)
        print(total)
        return total


# class Cart(CommonDateTime):
#     user = models.ForeignKey(
#         User,
#         verbose_name="유저",
#         on_delete=models.CASCADE
#     )
#     menus = models.ManyToManyField(
#         Menu,
#         verbose_name='메뉴',
#         blank=True)

#     total_price = models.DecimalField(
#         '총 가격',
#         default=0,
#         max_digits=100000,
#         decimal_places=2
#     )

#     objects = CartManager()

#     def __str__(self):
#         return str(self.id)

#     def get_total_price(self):
#         total_price = 0

#         for menu in self.menus.all():
#             total_price += menu.price

#         return total_price
