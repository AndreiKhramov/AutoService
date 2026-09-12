from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from automobile.models import Automobile
from automobile.validation import validate_vin_length, VALID_VIN_SYMBOLS, VALID_REG_NUMBER
from account.models import User


class AutoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(
        max_length=64
    )
    model = serializers.CharField(
        max_length=64
    )
    vin_number = serializers.CharField(
        validators=[UniqueValidator(queryset=Automobile.objects.all(), message='VIN number is a unique field'),
                    validate_vin_length,
                    VALID_VIN_SYMBOLS
        ]
    )
    registration_number = serializers.CharField(
        validators=[UniqueValidator(queryset=Automobile.objects.all(), message='Registration number is a unique field'),
                    VALID_REG_NUMBER
        ],
        max_length=16
    )
    user = serializers.SlugRelatedField(
        slug_field="email",
        queryset=User.objects.all(),
    )

    def create(self, validated_data):
        """
        Create and return a new `Automobile` instance, given the validated data.
        """
        return Automobile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Automobile` instance, given the validated data.
        """
        instance.brand = validated_data.get('brand', instance.brand)
        instance.model = validated_data.get('model', instance.model)
        instance.vin_number = validated_data.get('vin_number', instance.vin_number)
        instance.registration_number = validated_data.get('registration_number', instance.registration_number)
        instance.user = validated_data.get('user', instance.user)
        instance.save()
        return instance