from django.db import models


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