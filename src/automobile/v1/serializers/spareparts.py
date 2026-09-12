from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from automobile.models import Sparepart
from automobile.validation import price_validator


class SparepartSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    number = serializers.CharField(
        max_length=32,
        validators=[
            UniqueValidator(queryset=Sparepart.objects.all(), message='Sparepart number is a unique field')
        ]
    )
    name = serializers.CharField(
        max_length=128
    )
    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            price_validator
        ]
    )

    def create(self, validated_data):
        """
        Create and return a new `Automobile` instance, given the validated data.
        """
        return Sparepart.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Automobile` instance, given the validated data.
        """
        instance.number = validated_data.get('number', instance.number)
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance