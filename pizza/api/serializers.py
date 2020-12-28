
from rest_framework import serializers
from pizza.models import Products

class ProductsSerializerBase(serializers.ModelSerializer):

    class Meta:
        model = Products
        exclude = ['small_image','lage_image']
        read_only_fields = ['id']

class ProductsSerializerList(ProductsSerializerBase):
    image = serializers.FileField(source='small_image')


    class Meta(ProductsSerializerBase.Meta):
        exclude = ['ingredients','small_image','lage_image']

class ProductsSerializerDetail(ProductsSerializerBase):
    ingredients = serializers.ListField()
    image = serializers.FileField(source='lage_image')

    class Meta(ProductsSerializerBase.Meta):
        exclude = ['small_image','lage_image']



        