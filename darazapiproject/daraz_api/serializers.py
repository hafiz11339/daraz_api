from xml.etree.ElementInclude import include
from rest_framework import serializers
from .models import DarazData
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = DarazData
        fields = [
            'title',
            'img',
            'url',
            'get_price',
            'sku',
            'name'
        ]