from django.db import models

from config.common_datetime_model import CommonDateTime


class Menu(CommonDateTime):
    title = models.CharField(
        "메뉴 명",
        max_length=50
    )
    description = models.CharField(
        "메뉴 설명",
        max_length=50
    )
    price = models.DecimalField(
        "가격",
        max_digits=5,
        decimal_places=2
    )
    image = models.ImageField(
        "메뉴 이미지",
        upload_to=None,
        null=True,
        blank=True,
        max_length=None
    )
    active = models.BooleanField(
        "활성화 상태"
    )
