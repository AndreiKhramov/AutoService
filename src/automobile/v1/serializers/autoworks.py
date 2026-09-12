from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from automobile.models import Autowork


class AutoworkSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    number = serializers.CharField(
        max_length=32,
        validators=[
            UniqueValidator(queryset=Autowork.objects.all(), message='Autowork number is a unique field')
        ]
    )
    name = serializers.CharField(
        max_length=128
    )

    def create(self, validated_data):
        """
        Create and return a new `Automobile` instance, given the validated data.
        """
        return Autowork.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Automobile` instance, given the validated data.
        """
        instance.number = validated_data.get('number', instance.number)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance