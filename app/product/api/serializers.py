# Python imports

# Third party imports
from rest_framework import serializers

# Self imports
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"