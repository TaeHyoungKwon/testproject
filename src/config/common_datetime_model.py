from django.db import models


class CommonDateTime (models.Model):
    createa_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
