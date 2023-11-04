from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductTypeViewSet, ProductViewSet, ProductSpecificationViewSet, ProductSpecificationValueViewSet, ProductImageViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'product-types', ProductTypeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-specifications', ProductSpecificationViewSet)
router.register(r'product-specification-values', ProductSpecificationValueViewSet)
router.register(r'product-images', ProductImageViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]