from rest_framework import serializers
from products.models import Product, ProductCategory, LeadProductInterest




class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = (
            'id',
            'name',
            'parent'
        )

class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductCategory.objects.all(),
        source='category',
        write_only=True
    )
    class Meta:
        model = Product
        fields = (
            'id',
            'sku',
            'name',
            'description',
            'category',
            'type',
            'unit_of_measure',
            'base_price',
            'currency',
            'vat_rate',
            'is_active',
            'team',
            'category',
            'category_id'
        )
        read_only = ('id',)

class LeadProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    lead = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = LeadProductInterest
        fields = (
            'id',
            'lead',
            'product',
            'quantity',
            'estimated_value',
            'notes',
            'added_at',
            'discount'
        )

class LeadProductInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadProductInterest
        fields = (
            'id',
            'product',
            'quantity',
            'estimated_value',
            'notes',
            'discount'
        )


