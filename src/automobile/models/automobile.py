from automobile.validation import VALID_VIN_SYMBOLS, VALID_REG_NUMBER, validate_vin_length
from automobile.constants import BodyType
from config import settings
from config.models import BaseModel
from django.db import models


class Automobile(BaseModel):
    brand = models.CharField(
        verbose_name='Марка',
        max_length=64
    )
    model = models.CharField(
        verbose_name='Модель',
        max_length=64
    )
    vin_number = models.CharField(
        unique=True,
        verbose_name='VIN',
        validators=[
            VALID_VIN_SYMBOLS,
            validate_vin_length,
        ]
    )
    registration_number = models.CharField(
        unique=True,
        blank=True,
        null=True,
        validators=[
            VALID_REG_NUMBER
        ],
        verbose_name='Государственный номер',
        max_length=16
    )
    body_type = models.CharField(
        verbose_name='Тип кузова',
        blank=True,
        null=True,
        max_length=32,
        choices=BodyType.choices
    )
    chasses_number = models.CharField(
        unique=True,
        blank=True,
        null=True,
        validators= [
            VALID_VIN_SYMBOLS
        ]
    )
    body_number = models.CharField(
        unique=True,
        blank=True,
        null=True,
        validators=[
            VALID_VIN_SYMBOLS
        ]
    )
    colour = models.CharField(
        max_length=32,
        blank=True,
        null=True,
        verbose_name='Цвет'
    )
    vehicle_passport = models.CharField(
        verbose_name='Паспорт транспортного средства',
        unique=True,
        blank=True,
        null = True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='autos'
    )

    def __str__(self):
        return f'{self.brand} {self.model} {self.vin_number}'

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-id','-created_at']
        db_table = 'automobiles'
        verbose_name = 'Automobile'
        verbose_name_plural = 'Automobiles'


