from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required = True)
    price = serializers.DecimalField(max_digits = 10, decimal_places = 2)
    
    def validate_price(self, value):
        if value > 0:
            return value
        else:
            raise serializers.ValidationError("цена должна быть больше 0!")

    class Meta:
        model = Product
        fields = ('name', 'description', 'price')