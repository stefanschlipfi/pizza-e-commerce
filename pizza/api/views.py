from django.shortcuts import render

# Create your views here.
from rest_framework import  viewsets
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

# import serializers
from .serializers import ProductsSerializerList, ProductsSerializerDetail

#import models
from pizza.models import Products


class ProductsViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Products.
    """
    queryset = Products.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductsSerializerList
        return ProductsSerializerDetail
        