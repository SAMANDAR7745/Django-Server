from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.formfields import PhoneNumberField
from location_field.forms.plain import PlainLocationField


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.title


class Brend(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='food/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)])
    cat_id = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='foods')
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
