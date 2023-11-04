from rest_framework import viewsets
from .models import Category, ProductType, Product, ProductSpecification, ProductSpecificationValue, ProductImage
from .serializers import CategorySerializer, ProductTypeSerializer, ProductSerializer, ProductSpecificationSerializer, ProductSpecificationValueSerializer, ProductImageSerializer
from rest_framework.permissions import IsAdminUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from rest_framework import generics

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    
class ProductTypeListAPIView(generics.ListAPIView):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ProductListAPIView(generics.ListAPIView):  
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductTypeListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductSpecificationViewSet(viewsets.ModelViewSet):
    queryset = ProductSpecification.objects.all()
    serializer_class = ProductSpecificationSerializer
    
class ProductSpecificationListAPIView(generics.ListAPIView):
    queryset = ProductSpecification.objects.all()
    serializer_class = ProductSpecificationSerializer


class ProductSpecificationValueViewSet(viewsets.ModelViewSet):
    queryset = ProductSpecificationValue.objects.all()
    serializer_class = ProductSpecificationValueSerializer


class ProductSpecificationValueListAPIView(generics.ListAPIView):
    queryset = ProductSpecificationValue.objects.all()
    serializer_class = ProductSpecificationValueSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    
class ProductImageListAPIView(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer