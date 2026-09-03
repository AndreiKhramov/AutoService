from django.utils import timezone
from django.core.validators import RegexValidator
from rest_framework import serializers

validated_name = RegexValidator(r'^[a-zA-Z- ]+$', message="Use only Latin characters, spaces or hyphens.")
validated_email = RegexValidator(r'^[a-zA-Z0-9_.@]+$', message="Use only latin characters, digits, underscores, '@' or dot.")

def name_validator(value):
    value = value.strip()
    if len(value) < 2:
        raise serializers.ValidationError("Name must contain two or more symbols")

def email_validator(value):
    if value.count('@') != 1:
        raise serializers.ValidationError("You have to use one symbol of '@' in your email")
    if value.split('@')[0] in ['admin', 'root', 'system', 'support']:
        raise serializers.ValidationError("You can't use 'admin', 'root', 'system', 'support' as user part of email")

def birth_validator(value):
    today = timezone.localdate()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if value > today:
        raise serializers.ValidationError("You haven’t been born yet. Please enter a correct date of birth.")
    if not 18 <= age <= 120:
        raise serializers.ValidationError("Your age has to be between 18 and 120 years.")



