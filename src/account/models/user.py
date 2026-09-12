from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinValueValidator
from django.db import models

from account.constants import GenderChoice, CountryChoice
from account.models.managers.user import UserManager
from config.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    phone = models.CharField(
        max_length=16,
        unique=True,
        null=False
    )
    first_name = models.CharField(
        max_length=64
    )
    last_name = models.CharField(
        max_length=64
    )
    is_staff = models.BooleanField(
        default=False
    )
    email = models.EmailField(
        max_length=64,
        unique=True
    )
    USERNAME_FIELD = 'email'
    gender = models.CharField(
        max_length=1,
        choices=GenderChoice.choices
    )
    birth_date = models.DateField()
    country = models.CharField(
        verbose_name='Страна',
        default=CountryChoice.RUSSIA,
        choices=CountryChoice.choices
    )

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    class Meta:
        ordering = ['-id','-created_at']
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'