from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase

from apps.recipe import models


def sample_user(email='test@gmail.com', password='test123'):
    return get_user_model().objects.create_user(email=email, password=password)


class IngredientModelTests(APITestCase):
    def test_ingredient_str(self):
        """Test the ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='apple'
        )

        self.assertEqual(str(ingredient), ingredient.name)
