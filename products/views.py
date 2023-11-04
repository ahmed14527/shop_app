from rest_framework import viewsets
from .models import Category, ProductType, Product, ProductSpecification, ProductSpecificationValue, ProductImage
from .serializers import CategorySerializer, ProductTypeSerializer, ProductSerializer, ProductSpecificationSerializer, ProductSpecificationValueSerializer, ProductImageSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductSpecificationViewSet(viewsets.ModelViewSet):
    queryset = ProductSpecification.objects.all()
    serializer_class = ProductSpecificationSerializer

class ProductSpecificationValueViewSet(viewsets.ModelViewSet):
    queryset = ProductSpecificationValue.objects.all()
    serializer_class = ProductSpecificationValueSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer