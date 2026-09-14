from rest_framework import serializers

from automobile.models import Automobile, Sparepart, Autowork
from order.models import Order
from account.models import User

from decimal import Decimal
from order.constants import WORK_COST

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
        many=True,
        slug_field="number",
        queryset=Sparepart.objects.all(),
    )
    work = serializers.SlugRelatedField(
        many=True,
        slug_field="number",
        queryset=Autowork.objects.all(),
    )
    full_price = serializers.SerializerMethodField(read_only=True)

    def create(self, validated_data):
        """
        Create and return a new `Order` instance, given the validated data.
        """
        parts = validated_data.pop('part')
        works = validated_data.pop('work')

        order = Order.objects.create(**validated_data)

        order.part.set(parts)
        order.work.set(works)
        return order

    def update(self, instance, validated_data):
        """
        Update and return an existing `Order` instance, given the validated data.
        """
        parts = validated_data.pop('part')
        works = validated_data.pop('work')

        instance.user = validated_data.get('user', instance.user)
        instance.auto = validated_data.get('auto', instance.auto)

        instance.part.set(parts)
        instance.work.set(works)

        instance.save()
        return instance

    def get_full_price(self, obj):
        parts_price = sum(
            (part.price for part in obj.part.all()),
            Decimal("0.00"),
        )

        works_price = sum(
            (work.duration for work in obj.work.all()),
            Decimal("0.00"),
        ) * WORK_COST

        return parts_price + works_price