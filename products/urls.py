from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet, basename='category')
router.register('product-types', views.ProductTypeViewSet, basename='product-type')
router.register('products', views.ProductViewSet, basename='product')
router.register('product-specifications', views.ProductSpecificationViewSet, basename='product-specification')
router.register('product-specification-values', views.ProductSpecificationValueViewSet, basename='product-specification-value')
router.register('product-images', views.ProductImageViewSet, basename='product-image')

urlpatterns = [
    path('', include(router.urls)),
    path('categories/list/', views.CategoryListAPIView.as_view(), name='category-list'),
    path('product-types/list/', views.ProductTypeListAPIView.as_view(), name='product-type-list'),
    path('products/list/', views.ProductListAPIView.as_view(), name='product-list'),
    path('product-specifications/list/', views.ProductSpecificationListAPIView.as_view(), name='product-specification-list'),
    path('product-specification-values/list/', views.ProductSpecificationValueListAPIView.as_view(), name='product-specification-value-list'),
    path('product-images/list/', views.ProductImageListAPIView.as_view(), name='product-image-list'),
]