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
    price = models.PositiveSmallIntegerField(
        "가격"
    )
    image = models.ImageField(
        "메뉴 이미지",
        upload_to="%Y/%m/%d",
        null=True,
        blank=True,
    )
    active = models.BooleanField(
        "활성화 상태"
    )

    def __str__(self):
        return self.title + str(self.id)
