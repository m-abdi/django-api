from rest_framework import serializers
from . import models


class FoodsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Food
        fields = ['id', 'name', 'price', 'description', 'image']


class NewOrderSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Order
        fields = ['id', 'foods', 'data']