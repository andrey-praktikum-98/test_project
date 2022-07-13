from django.test import TestCase
from rest_framework import status

from .models import Food
from .models import FoodCategory


class FoodTestCase(TestCase):
    def setUp(self):
        FoodCategory.objects.create(name_ru="Напитки")
        FoodCategory.objects.create(name_ru="Выпечка")

        for i in range(3):

            Food.objects.create(
                category_id=1,
                name_ru=f"Кола{i}",
                code=i,
                internal_code=i,
                cost=i+100,
                is_publish=False,
            )

        Food.objects.create(
            category_id=1,
            name_ru="Фанта",
            code=100,
            internal_code=200,
            cost=123.50,
            is_publish=True,
        )

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_food_category(self):
        response = self.client.get("/api/v1/foods/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(len(response.data[0]["foods"]), 1)
