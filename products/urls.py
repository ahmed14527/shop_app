from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoryViewSet,
    ProductTypeViewSet,
    ProductSpecificationViewSet,
    ProductViewSet,
    ProductSpecificationValueViewSet,
    ProductImageViewSet,
)

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'product-types', ProductTypeViewSet)
router.register(r'product-specifications', ProductSpecificationViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-specification-values', ProductSpecificationValueViewSet)
router.register(r'product-images', ProductImageViewSet)

app_name = 'products'

urlpatterns = [
    path('', include(router.urls)),
]