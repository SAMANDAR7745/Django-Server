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
from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView, GenericAPIView
from main.serializers import *
from main.models import *
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status,filters, mixins
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import  IsAdminUser
import django_filters




# < ------ Category LIST ----- >
class CategoryCreateListView(APIView):
    def get(self, request: Request):
        products = Category.objects.all().order_by('-id')
        serializer = CategorySerializer(products, many=True)
        return render(request, "forms/list.html", context={"categorylist": serializer.data})

# < ------ Category Crute ------- >
class CategoryRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, pk):
        product = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(product)
        return render(request, 'forms/list.html', context={'categoryget': serializer.data})

    def put(self, request, pk):
        product = get_object_or_404(Category, pk=pk)
        data = request.data
        serializer = CategorySerializer(
            instance=product, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return render(request, context={"categoryput": serializer.data})
        else:
            return render(request, context={"categoryput": serializer.errors})

    def delete(self, request, pk):
        Category.objects.filter(id=pk).delete()
        return render(request, "forms/list.html", status=status.HTTP_204_NO_CONTENT, context={})


# < ----- Food list ------ >
class FoodCreateListView(APIView):
    def get(self, request: Request):
        food = Food.objects.all().order_by('-id')
        serializer = FoodSerializer(food, many=True)
        return render(request, 'forms/list.html', context={"food": serializer.data})


# < ----- Food crute ---- >
class FoodRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        serializer = FoodSerializer(food)
        return render(request, 'forms/list.html', context={"foodget": serializer.data})

    def put(self, request, pk):
        food = get_object_or_404(Food, pk=pk)
        data = request.data
        serializer = FoodSerializer(instance=food, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return render(request, context={"categoryput": serializer.data})
        else:
            return render(request, context={"categoryput": serializer.errors})

    def delete(self, request, pk):
        Food.objects.filter(id=pk).delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)


# < ----- Order list ------ >
class OrderCreateListView(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          GenericAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    """

    def get(self, request):
        food = Order.objects.all().order_by('-id')
        serializer = OrderSerializer(food, many=True)
        return render(request, 'forms/list.html', context={"orderget": serializer.data})

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["is_paid", 'shipping', "client"]


# < ----- Order crute ---- >
class OrderRetrieveUpdateDestroyAPIView(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        serializer = OrderSerializer(order)
        return render(request, 'forms/list.html', context={"orderget": serializer.data})

    def put(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        data = request.data
        serializer = OrderSerializer(instance=order, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return render(request,"forms/list.html'", context={"orderput": serializer.data})
        else:
            return render(request,"forms/list.html'", context={"orderput": serializer.errors})

    def delete(self, request, pk):
        Order.objects.filter(id=pk).delete()
        return Response(data={}, status=status.HTTP_204_NO_CONTENT)


# < ----- OrderItem list ------ >
class OrderItemCreateListView(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              GenericAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    """

    def get(self, request):
        orderi = OrderItem.objects.all().order_by('-id')
        serializer = OrderItemSerializer(orderi, many=True)
        return render(request, 'forms/list.html', context={"orderi": serializer.data})

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ["is_paid", 'shipping', "client"]


# < ----- OrderItem crute ------ >
class OrderItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAdminUser,)
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    location_field = 'pk'

# < ----- Client LIST ------ >
class ClientCreateListView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
    permission_classes = (IsAdminUser,)
    """
    Concrete view for listing a queryset or creating a model instance.
    """
    def get(self, request):
        orderi = Client.objects.all().order_by('-id')
        serializer = ClientSerializer(orderi, many=True)
        return render(request, 'forms/list.html', context={"client": serializer.data})

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



# < ----- Client crute ------ >
class ClientRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                         mixins.UpdateModelMixin,
                                         mixins.DestroyModelMixin,
                                         GenericAPIView):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """

    def get(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        serializer = ClientSerializer(client)
        return render(request, 'forms/list.html', context={"client": serializer.data})

    def put(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        data = request.data
        serializer = ClientSerializer(instance=client, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'forms/list.html', context={"client": serializer.data})
        else:
            return render(request, 'forms/list.html', context={"client": serializer.errors})

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    








# < ----- Members LIST ------ >
class MembersCreateListView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
    permission_classes = (IsAdminUser,)
    """
    Concrete view for listing a queryset or creating a model instance.
    """
    def get(self, request):
        members = Client.objects.all().order_by('-id')
        serializer = ClientSerializer(members, many=True)
        return render(request, 'forms/list.html', context={"members": serializer.data})

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



# < ----- Members crute ------ >
class MembersRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin,
                                         mixins.UpdateModelMixin,
                                         mixins.DestroyModelMixin,
                                         GenericAPIView):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """

    def get(self, request, pk):
        client = get_object_or_404(Members, pk=pk)
        serializer = MembersSerializer(client)
        return render(request, 'forms/list.html', context={"client": serializer.data})

    def put(self, request, pk):
        client = get_object_or_404(Members, pk=pk)
        data = request.data
        serializer = MembersSerializer(instance=client, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'forms/list.html', context={"client": serializer.data})
        else:
            return render(request, 'forms/list.html', context={"client": serializer.errors})

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)





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
