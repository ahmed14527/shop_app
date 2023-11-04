from django.contrib import admin
from .models import Category, ProductType, Product, ProductSpecification, ProductSpecificationValue, ProductImage

admin.site.register(Category)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(ProductSpecification)
admin.site.register(ProductSpecificationValue)
admin.site.register(ProductImage)