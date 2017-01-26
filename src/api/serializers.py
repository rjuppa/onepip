from django.conf.urls import url, include
from django.contrib.auth import get_user_model
from rest_framework import routers, serializers
from rest_framework.fields import IntegerField, DecimalField, DateTimeField

from trading.models import Price

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'is_staff')


class PriceSerializer(serializers.ModelSerializer):
    ask = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    bid = serializers.DecimalField(max_digits=10, decimal_places=2, coerce_to_string=False)
    volume = serializers.DecimalField(max_digits=16, decimal_places=8, coerce_to_string=False)
    created_at = DateTimeField(format='%Y-%m-%d %H:%M:%S', input_formats=None)

    class Meta:
        model = Price
        fields = ('created_at', 'ask', 'bid', 'volume')
