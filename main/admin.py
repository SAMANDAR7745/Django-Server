from django.contrib import admin
from .models import Category, Client, Order, OrderItem, Food, Members, Comment

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Client)
admin.site.register(Members)
admin.site.register(Comment)
