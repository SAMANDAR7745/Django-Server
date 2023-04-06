from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.formfields import PhoneNumberField
from location_field.forms.plain import PlainLocationField


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return f'{self.title}{self.slug}' 


class Food(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='food/image', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='foods')

    def __str__(self):
        return f'{self.title}{self.desc}{self.image.url}' 


class Order(models.Model):
    PICKUP = 'pickup'
    DELIVERY = "delivery"
    SHIPPING_TYPES = (
        (PICKUP, 'Pick Up'),
        (DELIVERY, 'Delivery')
    )
    client = models.ForeignKey(
        'Client', on_delete=models.CASCADE, related_name='orders')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    shipping = models.CharField(
        max_length=10, choices=SHIPPING_TYPES, default=DELIVERY)
    location = PlainLocationField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.client.full_name} - {self.pk}'


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    food = models.ForeignKey(
        Food, on_delete=models.CASCADE, related_name="order_items")
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Client(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField()
    image = models.ImageField(upload_to="post/images/", null=True, blank=True)

    def __str__(self):
        return f"{self.full_name}{self.image.url}"

class Members(models.Model):
    full_name = models.CharField(max_length=100)
    Designation = models.URLField()
    image = models.ImageField(upload_to="post/images/", null=True, blank=True)
    
    def __str__(self):
        return self.full_name
    
class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
