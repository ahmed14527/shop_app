from rest_framework import serializers
from .models import Category, ProductType, ProductSpecification, Product, ProductSpecificationValue, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'parent', 'is_active']


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id', 'name', 'is_active']


class ProductSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecification
        fields = ['id', 'product_type', 'name']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_type', 'category', 'title', 'description', 'slug', 'regular_price', 'discount_price',
                  'is_active', 'created_at', 'updated_at', 'users_wishlist']


class ProductSpecificationValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSpecificationValue
        fields = ['id', 'product', 'specification', 'value']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image', 'alt_text', 'is_feature', 'created_at', 'updated_at']