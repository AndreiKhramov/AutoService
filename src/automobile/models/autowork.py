from django.db import models
from automobile.constants import Workshop
from config.models import BaseModel


class Autowork(BaseModel):
    number = models.CharField(
        verbose_name='Номер работы',
        max_length=100
    )
    name = models.CharField(
        verbose_name='Название работы',
        max_length=100
    )
    duration = models.PositiveIntegerField(
        verbose_name='Продолжительность работы',
        default=1
    )
    workshop = models.CharField(
        verbose_name='Цех',
        max_length=25,
        choices=Workshop.choices,
        default=Workshop.LOCKSMITH
    )
    # work_order = models.ManyToManyField('order.Order', through='OrderWork')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['name']
        db_table = 'autoworks'
        verbose_name = 'Autowork'
        verbose_name_plural = 'Autoworks'
