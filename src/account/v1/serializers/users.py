from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'gender', 'id', 'phone']


class UserFuncSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(
        max_length=64,
        validators=[UniqueValidator(queryset=User.objects.all(), message='Email is a unique field, already exists')]
    )
    first_name = serializers.CharField(
        max_length=64
    )
    last_name = serializers.CharField(
        max_length=64
    )
    gender = serializers.CharField(
        max_length=1
    )
    phone = serializers.CharField(
        max_length=16,
        validators=[UniqueValidator(queryset=User.objects.all(), message='Phone is a unique field')]
    )

    def validate_phone(self, phone):
        """
        Check is phone_number correct.
        """
        if not all(
                [
                    phone.startswith('+'),
                    len(phone) == 12,
                    phone[1:].isdigit()
                ]
        ):

            raise serializers.ValidationError("Phone number is not correct")
        return phone

