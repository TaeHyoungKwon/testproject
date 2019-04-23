from decimal import Decimal
from django.conf import settings
from django.db import models

from config.common_datetime_model import CommonDateTime
from menus.models import Menu

User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        print(qs)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            new_obj = True
            print(request.user)
            cart_obj = Cart.objects.new(user=request.user)
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user_obj
        return self.model.objects.create(user=user_obj)


class Cart(CommonDateTime):
    user = models.ForeignKey(
        User,
        verbose_name="유저",
        on_delete=models.CASCADE
    )
    menus = models.ManyToManyField(
        Menu,
        verbose_name='메뉴',
        blank=True)

    total_price = models.DecimalField(
        '총 가격',
        default=0.00,
        max_digits=100,
        decimal_places=2
    )

    objects = CartManager()

    def __str__(self):
        return str(self.id)
