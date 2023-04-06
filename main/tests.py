from django.test import TestCase
from  main.models import Category, Food


class FoodModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Food.objects.create(title='first todo', desc="",price=12,rating=4,category=4)

    def test_title_content(self):
        todo = Food.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assertEqual(expected_object_name, 'first todo')
            
            
    def test_desc_content(self):
        todo = Food.objects.get(id=1)
        expected_object_name = f'{todo.desc}'
        self.assertEqual(expected_object_name, '')


    def test_price_content(self):
        todo = Food.objects.get(id=1)
        expected_object_name = f'{todo.price}'
        self.assertEqual(expected_object_name, 12)

    def test_rating_content(self):
        todo = Food.objects.get(id=1)
        expected_object_name = f'{todo.rating}'
        self.assertEqual(expected_object_name, 4)
        