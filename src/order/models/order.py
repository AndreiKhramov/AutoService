from django.db import models

from config import settings
from config.models import BaseModel


class Order(BaseModel):
    number = models.PositiveIntegerField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='order'
    )
    auto = models.ForeignKey(
        to='automobile.Automobile',
        on_delete=models.CASCADE,
        related_name='order'
    )
    part = models.ManyToManyField(
        to='automobile.Sparepart'
    )
    work = models.ManyToManyField(
        to='automobile.Autowork'
    )
    full_price = models.DecimalField(
        verbose_name='Общая цена',
        max_digits=10,
        decimal_places=2,
        default=0
    )
    full_time = models.PositiveIntegerField(
        verbose_name='Общая продолжительность работ',
        default=0
    )

    def __str__(self):
        return f'{self.number}'

    class Meta:
        ordering = ['number', '-created_at']
        db_table = 'orders'
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'