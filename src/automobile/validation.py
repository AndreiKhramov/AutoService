from django.core.validators import RegexValidator

VALID_VIN_SYMBOLS = RegexValidator(
    r'^[A-HJ-NR-ZP0-9]*$',
    'Только буквенно-цифровые символы, исключая буквы I, O и Q.'
)

VALID_REG_NUMBER = RegexValidator(
    r'^[A-ZАВЕКМНОРСТУХ0-9]+$',
    'Только буквенно-цифровые символы латинского алфавита или буквы АВЕКМНОРСТУХ русского алфавита.'
)
