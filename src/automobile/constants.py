from django.core.validators import RegexValidator
from django.db import models

VALID_VIN_SYMBOLS = RegexValidator(
    r'^[A-HJ-NR-ZP0-9]*$',
    'Только буквенно-цифровые символы, исключая буквы I, O и Q.'
)

VALID_REG_NUMBER = RegexValidator(
    r'^[A-ZАВЕКМНОРСТУХ0-9]+$',
    'Только буквенно-цифровые символы латинского алфавита или буквы АВЕКМНОРСТУХ русского алфавита.'
)


class BodyType(models.TextChoices):
    SEDAN = 'sedan', 'Седан'
    HATCHBACK = 'hatchback', 'Хэтчбэк'
    STATIONWAGON = 'station wagon', 'Универсал'
    COUPE = 'coupe', 'Купе'
    PICKUP = 'pickup', 'Пикап'
    CONVERTIBLE = 'convertible', 'Кабриолет'
    ROADSTER = 'roadster', 'Родстер'
    MINIVAN = 'minivan', 'Минивэн'
    SUV =  'SUV', 'Внедорожник'
    CROSSOVER = 'crossover', 'Кроссовер'
    LIMOUSINE = 'limousine', 'Лимузин'


class Workshop(models.TextChoices):
    BODYSHOP = 'bodyshop', 'Кузовной'
    LOCKSMITH = 'locksmith', 'Слесарный'