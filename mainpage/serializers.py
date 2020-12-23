from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Shopserializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
