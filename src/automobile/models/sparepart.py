from django.db import models


class Sparepart(models.Model):
    part_name = models.CharField(verbose_name='Деталь', max_length=100)
    part_number = models.CharField(verbose_name='Номер детали', max_length=100)
    part_brand = models.CharField(verbose_name='Производитель', max_length=100)
    part_image = models.ImageField()
    ''' Сделать таблицу поставщиков и связь с part_vendor'''
    part_vendor = models.CharField(verbose_name='Поставщик', max_length=100)
    price = models.DecimalField(max_digits=10, verbose_name='Цена', decimal_places=2, )
    # part_order = models.ManyToManyField('order.Order', through='OrderPart')

