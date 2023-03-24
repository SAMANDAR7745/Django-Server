from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("category/",CategoryCreateListView.as_view(), name="category" ),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category_detail'),
    path("product/", ProductCreateListView.as_view(), name="product"),
    path('product/<int:pk>/',
         ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_detail'),
    path("brend/", BrendCreateListView.as_view(),name='brend'),
    path('brend/<int:pk>/', BrendUpdateDestroyAPIView.as_view(),
         name='brend_detail'),

]
