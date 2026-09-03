from django.core.validators import RegexValidator, ValidationError
from django.utils.translation import gettext_lazy as _

VALID_VIN_SYMBOLS = RegexValidator(
    r'^[A-HJ-NR-ZP0-9]*$',
    'Только буквенно-цифровые символы, исключая буквы I, O и Q.'
)

VALID_REG_NUMBER = RegexValidator(
    r'^[A-ZАВЕКМНОРСТУХ0-9]+$',
    'Только буквенно-цифровые символы латинского алфавита или буквы АВЕКМНОРСТУХ русского алфавита.'
)

def validate_vin_length(value):
    if len(value) != 17:
        raise ValidationError(
            _(f'VIN {value} должен содержать ровно 17 символов!'),
            params={'value': value},
        )