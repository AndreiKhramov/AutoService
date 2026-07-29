from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinValueValidator
from django.db import models

from account.constants import GenderChoice, CountryChoice
from account.models.managers.user import UserManager
from config.models import BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    phone = models.CharField(max_length=255, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(max_length=64, unique=True)
    USERNAME_FIELD = 'email'
    gender = models.CharField(blank=True, max_length=1, choices=GenderChoice.choices)
    age = models.PositiveSmallIntegerField(null=True, blank=True, validators=[MinValueValidator(18)], help_text='Возраст (не менее 18 лет)')
    country = models.CharField(verbose_name='Страна', default=CountryChoice.RUSSIA, choices=CountryChoice.choices)

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    class Meta:
        ordering = ["-id","-created_at"]
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"