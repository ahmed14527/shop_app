from rest_framework import viewsets, permissions
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer
from django.http import JsonResponse
from django.views import View
from .models import Favorite, Product
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@method_decorator(login_required, name='dispatch')
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    
    
@method_decorator(login_required, name='dispatch')
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
@method_decorator(login_required, name='dispatch')
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer



