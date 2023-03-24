from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("id",)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("id", "title", "desc", "image", "price", "rating", "cat_id", 'brend')
        read_only_fields = ('id', 'cat_id', 'brend')


class BrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brend
        fields = "__all__"
        read_only_fields = ("",)
