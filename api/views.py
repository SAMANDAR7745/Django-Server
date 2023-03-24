from django.shortcuts import render

from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from main.serializers import *
from main.models import *
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import django_filters
from rest_framework import filters


class CategoryCreateListView(APIView):
    def get(self, request: Request):
        products = Category.objects.all().order_by('-id')
        serializer = CategorySerializer(products, many=True)
        return Response(data={"category": serializer.data})

    def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.query_params.get("name")
        if name is not None:
            return Category.objects.filter(title_icontains=name)
        return queryset


class CategoryRetrieveUpdateDestroyAPIView(APIView):
    

    def get(self, pk):
        product = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(product)
        return Response(data=serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Category, pk=pk)
        data = request.data
        serializer = CategorySerializer(
            instance=product, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def delete(self, pk):
        Category.objects.filter(id=pk).delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)


class ProductCreateListView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["brend"]


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    location_field = 'pk'




class BrendCreateListView(ListCreateAPIView):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["title"]


class BrendUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer
    location_field = 'pk'
