from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

# import serializers
from .serializers import ProductsSerializerList, ProductsSerializerDetail

#import models
from pizza.models import Products


class ProductsViewSet(ModelViewSet):
    """
    A viewset for viewing and editing Products.
    """
    queryset = Products.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductsSerializerList
        return ProductsSerializerDetail
        