from django.db import models

from config.models import BaseModel


class Sparepart(BaseModel):
    name = models.CharField(
        verbose_name='Деталь',
        max_length=128
    )
    number = models.CharField(
        verbose_name='Номер детали',
        max_length=32
    )
    brand = models.CharField(
        verbose_name='Производитель',
        max_length=64
    )
    image = models.ImageField()
    # TODO ''' Сделать таблицу поставщиков и связь с part_vendor'''
    vendor = models.CharField(
        verbose_name='Поставщик',
        max_length=128
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=10,
        decimal_places=2,
    )
    # part_order = models.ManyToManyField('order.Order', through='OrderPart')

    def __str__(self):
        return f'{self.number} {self.brand} {self.name}'

    class Meta:
        ordering = ['name']
        db_table = 'spareparts'
        verbose_name = 'Sparepart'
        verbose_name_plural = 'Spareparts'