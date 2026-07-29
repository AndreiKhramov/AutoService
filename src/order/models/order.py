import datetime

from django.db import models

from automobile.models.autowork import Autowork
from automobile.models.sparepart import Sparepart
from config import settings
from automobile.models.automobile import Automobile



class Order(models.Model):
    order_number = models.IntegerField()
    order_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order')
    order_auto = models.ForeignKey(Automobile, on_delete=models.CASCADE, related_name='order')
    order_part = models.ManyToManyField(Sparepart, through='OrderPart')
    order_work = models.ManyToManyField(Autowork, through='OrderWork')
    full_price = models.DecimalField(max_digits=10, verbose_name='Общая цена', decimal_places=2,)
    full_time = models.DurationField(verbose_name='Общая продолжительность работ', default=datetime.timedelta(minutes=1))


class OrderWork(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    work = models.ForeignKey(Autowork, on_delete=models.CASCADE)


class OrderPart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    part = models.ForeignKey(Sparepart, on_delete=models.CASCADE)