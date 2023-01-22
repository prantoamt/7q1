# Python imports

# Third party imports
from rest_framework import serializers

# Self imports
from company.models import Company
from product.models import Product
from companyproduct.models import CompanyProduct
from product.api.serializers import ProductSerializer


class CompanySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Company
        fields = ['id', 'name', 'url', 'country', 'is_deleted', 'created_at', 'updated_at', 'products']

    def get_products(self, obj: object):
        product_ids = CompanyProduct.objects.filter(company_id=obj.id).values_list('product')
        products = Product.objects.filter(id__in=product_ids)
        return ProductSerializer(products, many=True).data