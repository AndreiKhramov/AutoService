from django.db import models

class Vehicle(models.Model):
    class VehicleType(models.TextChoices):
        GROUNDTYPE = 'ground', 'Наземный'
        WATERTYPE = 'water', 'Водный'
        AIRTYPE = 'air', 'Воздушный'

    brand = models.CharField(verbose_name='Марка', max_length=100)
    vehicle_type = models.CharField(
        max_length=20,
        choices=VehicleType.choices,
        default=VehicleType.GROUNDTYPE,
        verbose_name='Тип транспорта',
    )