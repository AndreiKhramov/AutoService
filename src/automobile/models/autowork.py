from django.db import models
import datetime
from automobile.constants import Workshop


class Autowork(models.Model):
    work_number = models.CharField(verbose_name='Номер работы', max_length=100)
    work_name = models.CharField(verbose_name='Название работы', max_length=100)
    work_duration = models.DurationField(verbose_name='Продолжительность работы', default=datetime.timedelta(minutes=1))
    workshop = models.CharField(max_length=25, choices=Workshop.choices, default=Workshop.LOCKSMITH)
    # work_order = models.ManyToManyField('order.Order', through='OrderWork')

