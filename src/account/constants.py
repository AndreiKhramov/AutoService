from django.db import models
from django.utils.translation import gettext_lazy as _

class GenderChoice(models.TextChoices):
    MALE = 'M', _('Мужской')
    FEMALE = 'F', _('Женский')


class CountryChoice(models.TextChoices):
    RUSSIA = 'RU', _('Россия')
    BELARUS = 'BE', _('Беларусь')
    UKRAINE = 'UA', _('Украина')
    KAZAKHSTAN = 'KZ', _('Казахстан')
    UZBEKISTAN = 'UZ', _('Узбекистан')
    GEORGIA = 'GE', _('Грузия')
    AZERBAIJAN = 'AZ', _('Азербайджан')
    LITHUANIA = 'LT', _('Литва')
    LATVIA = 'LV', _('Латвия')
    ESTONIA = 'EE', _('Эстония')
    ARMENIA = 'AM', _('Армения')
    TURKMENISTAN = 'TM', _('Туркменистан')
    KYRGYZSTAN = 'KG', _('Киргизия')
    MOLDOVA = 'MD', _('Молдавия')
    TAJIKISTAN = 'TJ', _('Таджикистан')
