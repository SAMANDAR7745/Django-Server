from .models import *
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("id",)


class FoodSerializer(serializers.ModelSerializer):
    cat = serializers.SerializerMethodField()

    class Meta:
        model = Food
        fields = ('title', 'desc', 'image', 'price', 'rating', 'category', 'cat')
        read_only_fields = ("id", 'cat')

    def get_cat(self, obj):
        return obj.category.title


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all"
        read_only_fields = ("id","image")


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'client', 'total_price', 'is_paid', 'shipping', 'created', 'updated', 'client_name')
        read_only_fields = ("id",)



class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    food = FoodSerializer()

    class Meta:
        model = OrderItem
        fields = "__all__"
        read_only_fields = ("id",)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ("id",)


class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = "__all__"
        read_only_fields = ("id",)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("id",)