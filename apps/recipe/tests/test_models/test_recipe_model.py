from django.contrib.auth import get_user_model
from django.test import TestCase

from apps.recipe import models


def sample_user(email='test@gmail.com', password='test123'):
    return get_user_model().objects.create_user(email=email, password=password)


class RecipeModelTests(TestCase):
    def test_recipe_str(self):
        """Test the string representation of a Recipe model."""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Test Recipe',
            time_minutes=10,
            price=10.00
        )

        self.assertEqual(str(recipe), 'Test Recipe')
