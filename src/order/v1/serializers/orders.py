from rest_framework import serializers

from automobile.models import Automobile, Sparepart, Autowork
from order.models import Order
from account.models import User


class OrderSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    user = serializers.SlugRelatedField(
        slug_field="email",
        queryset=User.objects.all(),
    )
    auto = serializers.SlugRelatedField(
        slug_field="vin_number",
        queryset=Automobile.objects.all(),
    )
    part = serializers.SlugRelatedField(
        slug_field="number",
        queryset=Sparepart.objects.all(),
    )
    work = serializers.SlugRelatedField(
        slug_field="number",
        queryset=Autowork.objects.all(),
    )
    full_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
    )


    def create(self, validated_data):
        """
        Create and return a new `Automobile` instance, given the validated data.
        """
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Automobile` instance, given the validated data.
        """
        instance.user = validated_data.get('user', instance.user)
        instance.auto = validated_data.get('auto', instance.auto)
        instance.part = validated_data.get('part', instance.part)
        instance.work = validated_data.get('work', instance.work)
        instance.save()
        return instance