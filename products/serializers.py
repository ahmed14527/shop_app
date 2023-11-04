from rest_framework import serializers
from .models import Category, ProductType, Product, ProductSpecification, ProductSpecificationValue, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = '__all__'

class ProductSpecificationValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecificationValue
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'