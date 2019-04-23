from django.conf import settings
from django.db import models

from config.common_datetime_model import CommonDateTime

from cart.models import Cart

ORDER_STATUS = (
    ('created', '생성됨'),
    ('paid', '결제됨'),
    ('shipped', '발송됨'),
)

User = settings.AUTH_USER_MODEL


class Order(CommonDateTime):
    billing_profile = models.ForeignKey(
        User,
        verbose_name="구매 고객",
        on_delete=models.CASCADE
    )
    order_id = models.CharField(
        "주문 번호",
        max_length=50
    )
    shipped_address = models.TextField(
        "배달 주소"
    )
    cart = models.ForeignKey(
        Cart,
        verbose_name="장바구니",
        on_delete=models.CASCADE
    )
    status = models.CharField(
        "주문 상태",
        max_length=50
    )
    total = models.DecimalField(
        "총 금액",
        max_digits=5,
        decimal_places=2
    )
    active = models.BooleanField(
        "활성 상태"
    )
