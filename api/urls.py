from django.urls import path
from . views_user import *
from .views import *
from .views_templates import *
from .auth import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
user_list = UserViewSet.as_view({"get": "list", "post": "create"})
user_detail = UserViewSet.as_view({'get': "retrieve", 'put': "update", "delete": "destroy"})

urlpatterns = [
    path('cats/', CategoryCreateListView.as_view(), name="cats"),
    path('cats/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name="cats_detail "),
    path('food/', FoodCreateListView.as_view(), name='food'),
    path('food/<int:pk>/', FoodRetrieveUpdateDestroyAPIView.as_view(), name='food_detail'),
    path('order/', OrderCreateListView.as_view(), name='order'),
    path('order/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order_detail'),
    path('order_items/', OrderItemCreateListView.as_view(), name='order_items'),
    path('order_items/<int:pk>/', OrderItemRetrieveUpdateDestroyAPIView.as_view(), name='order_items_detail'),
    path('client/', ClientCreateListView.as_view(), name='client'),
    path('client/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client_detail'),
    path('',HomeCreateListView.as_view(), name='index'),
    path('about/', AboutCreateListView.as_view(), name='about'),
    path('service/', service, name='service'),
    path('menu/', MenuCreateListView.as_view(), name='menu'),
    path('booking/', booking, name='booking'),
    path('tur_team/', tur_team, name='tur_team'),
    path('testimonial/', testimonial, name='testimonial'),
    path('contact/', contact, name='contact'),
    path('registor/', RegisterUser.as_view(), name="registor"),
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', LogoutUser.as_view(), name="logout"),
    path('password_reset/', PasswordReset.as_view(), name='password_reset'),
    path('profile/', UserView.as_view(), name='profile'),
    path('profile/update/', UserUpdateView.as_view(), name='update_profile'),
    path('user/delete/', DeleteUser.as_view(), name='delete')


] + router.urls
