from django.core.validators import MinLengthValidator, MaxLengthValidator
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from account.models import User
from account.validation import name_validator, email_validator, validated_email, validated_name, birth_validator


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all(), message='Email is a unique field, already exists'),
            MinLengthValidator(4),
            MaxLengthValidator(30),
            validated_email,
            email_validator
        ]
    )
    first_name = serializers.CharField(
        max_length=64,
        validators=[
            validated_name,
            name_validator
        ]
    )
    last_name = serializers.CharField(
        max_length=64,
        validators=[
            validated_name,
            name_validator
        ]
    )
    gender = serializers.CharField(
        max_length=1
    )
    phone = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all(), message='Phone is a unique field'),
            MinLengthValidator(12),
            MaxLengthValidator(12)
        ]
    )
    birth_date = serializers.DateField(
        validators=[
            birth_validator
        ]
    )
    # password = serializers.CharField(
    #     max_length=64,
    #     validators=[validated_name]
    # )

    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        user = User.objects.create(**validated_data)
        # try:
        #     user.full_clean()
        # except DjangoValidationError as error:
        #     raise serializers.ValidationError(error.message_dict) from error
        # user.save()
        return user

    def update(self, instance, validated_data):
        """
        Update and return an existing `User` instance, given the validated data.
        """
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone = validated_data.get('phone', instance.phone)
        # try:
        #     instance.full_clean()
        # except DjangoValidationError as error: raise serializers.ValidationError(error.message_dict) from error
        # instance.save()
        return instance

    def validate_phone(self, value):
        """
        Check is phone_number correct.
        """
        if not value:
            raise serializers.ValidationError("Phone number must not be empty")
        if not value.startswith('+'):
            raise serializers.ValidationError("Phone number must starts with '+'")
        if not value[1:].isdigit():
            raise serializers.ValidationError("Phone number must contain only digits")
        return value

    # def validate_gender(self, value):
    #     """
    #     Check is gender correct.
    #     """
    #     if not value:
    #         raise serializers.ValidationError("Gender must not be empty")
    #     if not 'M' or not 'F':
    #         raise serializers.ValidationError("Gender must be only 'M' - Male or 'F' - Female")
    #     return value
