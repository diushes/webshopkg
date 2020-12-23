from rest_framework import serializers
from .models import *


class Shopserializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
