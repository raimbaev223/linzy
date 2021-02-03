from rest_framework import viewsets


from .serializers import CategorySerializer, ProductSerializer
from ..models import Category, Product


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.prod.all()
    serializer_class = ProductSerializer
