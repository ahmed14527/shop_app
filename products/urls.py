from django.urls import path, include
from rest_framework import routers
from .views import (CategoryViewSet, ProductTypeViewSet,
                    ProductViewSet, ProductSpecificationViewSet,
                    ProductSpecificationValueViewSet, ProductImageViewSet,
                    CategoryListAPIView,ProductTypeListAPIView,
                    ProductListAPIView,ProductSpecificationListAPIView,
                    ProductSpecificationValueListAPIView,ProductImageListAPIView)

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'product-types', ProductTypeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-specifications', ProductSpecificationViewSet)
router.register(r'product-specification-values', ProductSpecificationValueViewSet)
router.register(r'product-images', ProductImageViewSet)

urlpatterns = [
    path('categories/list/',CategoryListAPIView.as_view(), name='category-list'),
    path('product-types/list/',ProductTypeListAPIView.as_view(), name='product-type-list'),
    path('products/list/', ProductListAPIView.as_view(), name='product-list'),
    path('product-specifications/list/', ProductSpecificationListAPIView.as_view(), name='product-specification-list'),
    path('product-specification-values/list/', ProductSpecificationValueListAPIView.as_view(), name='product-specification-value-list'),
    path('product-images/list/', ProductImageListAPIView.as_view(), name='product-image-list'),
    path('', include(router.urls)),

]