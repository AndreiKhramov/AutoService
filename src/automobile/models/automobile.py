from django.core.validators import MinLengthValidator

from automobile.validation import  VALID_VIN_SYMBOLS, VALID_REG_NUMBER
from automobile.constants import BodyType
from config import settings
from config.models import BaseModel
from django.db import models


class Automobile(BaseModel):
    brand = models.CharField(verbose_name='Марка', max_length=100)
    model = models.CharField(verbose_name='Модель', max_length=100)
    VIN_number = models.CharField(
        unique=True, verbose_name='VIN', max_length=17,
        validators=[ VALID_VIN_SYMBOLS, MinLengthValidator(17, message='VIN должен содержать ровно 17 символов.')]
    )
    registartion_number = models.CharField(
        unique=True, validators=[VALID_REG_NUMBER], verbose_name='Государственный номер', max_length=15
    )
    body_type = models.CharField(max_length=50, choices=BodyType.choices, verbose_name='Тип кузова', )
    chasses_number = models.CharField(unique=True, validators= [VALID_VIN_SYMBOLS], )
    body_number = models.CharField(unique=True, validators= [VALID_VIN_SYMBOLS], )
    colour = models.CharField(max_length=50, verbose_name='Цвет')
    vehicle_passport = models.CharField(unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='auto')

    def __str__(self):
        return f'{self.brand} {self.model} {self.VIN_number}'

    class Meta:
        ordering = ['-id','-created_at']
        db_table = 'automobiles'
        verbose_name = 'Automobile'
        verbose_name_plural = 'Automobiles'


